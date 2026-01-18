# Despliegue DECIDE en Render con CI/CD

## Descripción general

Se ha configurado el despliegue automático de DECIDE en Render mediante GitHub Actions y CI/CD. La aplicación se despliega automáticamente cuando se realiza un push a las ramas configuradas.

## Archivos creados

### 1. **build.sh** - Script de construcción
Script que se ejecuta durante el despliegue en Render:
```bash
#!/bin/bash
set -e

cd decide

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Ejecutar migraciones
python manage.py migrate --noinput

echo "Build completado exitosamente"
```

**Funcionalidad:**
- Cambia al directorio `decide`
- Instala todas las dependencias desde `requirements.txt`
- Recolecta archivos estáticos automáticamente
- Ejecuta migraciones de Django
- Confirma que el build fue exitoso

### 2. **.github/workflows/render-deploy.yml** - Pipeline de CI/CD
Workflow que automatiza las pruebas y el despliegue:

**Trigger:** Push a las ramas `egc_test`, `main`, `master`

**Pasos del workflow:**
1. Checkout del código
2. Instalación de dependencias
3. Ejecución de tests (solo si el código es válido)
4. Trigger de despliegue en Render si los tests pasan
5. Confirmación de despliegue exitoso

## Configuración de Render

### Paso 1: Crear la aplicación en Render

1. Ir a https://render.com y conectar tu cuenta de GitHub
2. Crear una nueva "Web Service"
3. Seleccionar el repositorio `EGC-2324-1140-antjimde`
4. Configurar:
   - **Name:** decide (o el nombre que prefieras)
   - **Runtime:** Python 3
   - **Region:** Frankfurt (u otra cercana)
   - **Plan:** Free

### Paso 2: Configurar comandos de build y start

En la configuración de Render, establecer:

**Build Command:**
```bash
bash build.sh
```

**Start Command:**
```bash
cd decide && gunicorn decide.wsgi:application --bind 0.0.0.0:$PORT
```

### Paso 3: Configurar variables de entorno

En Render Dashboard, añadir las siguientes variables de entorno:

```
DEBUG=False
ALLOWED_HOSTS=*.onrender.com
SECRET_KEY=<tu_clave_secreta_segura>
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
```

Para la base de datos PostgreSQL, Render proporciona automáticamente `DATABASE_URL` si añades una base de datos.

### Paso 4: Conectar con GitHub Secrets

En tu repositorio de GitHub, ir a Settings > Secrets and variables > Actions

Añadir dos secrets:

1. **RENDER_SERVICE_ID**
   - Encontrar en la URL de tu servicio: `https://dashboard.render.com/web/srv-xxxxxxxxxxxxxxxx`
   - El valor es todo lo que va después de `/web/`

2. **RENDER_API_KEY**
   - Generar en Render Dashboard > Account Settings > API Keys
   - Copiar la clave generada

## Flujo de despliegue

### Despliegue automático

1. **Hacer cambios en el código**
2. **Commit y push** a alguna de las ramas configuradas:
   ```bash
   git add .
   git commit -m "descripción de cambios"
   git push origin egc_test
   ```

3. **GitHub Actions se activa automáticamente:**
   - ✅ Descarga el código
   - ✅ Instala dependencias
   - ✅ Ejecuta los tests
   - Si todo pasa → ✅ Dispara despliegue en Render

4. **Render recibe la solicitud de despliegue:**
   - Descarga el código
   - Ejecuta `bash build.sh`
   - Instala dependencias, recolecta estáticos, ejecuta migraciones
   - Inicia la aplicación con Gunicorn
   - La aplicación está disponible en `https://<nombre-servicio>.onrender.com`

## Verificar el despliegue

### En GitHub Actions
1. Ve a tu repositorio en GitHub
2. Haz clic en la pestaña "Actions"
3. Verifica que el workflow "Deploy to Render" se ejecute
4. Si los tests fallan, se mostrará el error

### En Render
1. Ve a https://dashboard.render.com
2. Selecciona tu servicio "decide"
3. En "Deployments" verás el historial de despliegues
4. Haz clic en un despliegue para ver los logs

### Acceder a la aplicación
Una vez desplegada, será accesible en:
```
https://<nombre-servicio>.onrender.com/admin
```

Credenciales (si creaste manualmente un superuser):
- Usuario: `admin`
- Contraseña: `admin`

## Comandos útiles para desplegar manualmente

### Desde Render Dashboard
- Ve a tu servicio
- Haz clic en "Redeploy" para forzar un nuevo despliegue

### Desde GitHub
- Realiza un push a cualquiera de las ramas configuradas
- El workflow se ejecutará automáticamente

## Solucionar problemas

### Los tests fallan en GitHub Actions
- Verifica que `requirements.txt` esté actualizado
- Revisa los logs en GitHub Actions para ver los errores

### El despliegue en Render falla
- Verifica las variables de entorno en Render
- Revisa los logs en Render Dashboard
- Asegúrate de que la base de datos esté correctamente configurada

### La aplicación no inicia
- Verifica que el comando start sea correcto
- Comprueba que todas las migraciones se ejecuten correctamente
- Revisa los logs de Render

## Notas importantes

- **Plan free de Render:** La aplicación se pausa después de 15 minutos sin actividad
- **Base de datos:** Debes crear una base de datos PostgreSQL en Render (también disponible en plan free)
- **Tests obligatorios:** Los tests deben pasar para que se despliegue
- **Migraciones automáticas:** Se ejecutan automáticamente en cada despliegue
- **Archivos estáticos:** Se recopilan automáticamente en cada despliegue
