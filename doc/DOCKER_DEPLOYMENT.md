# Despliegue DECIDE con Docker

## Resumen de cambios realizados

Se han realizado las siguientes modificaciones en los archivos de configuración de Docker para que el repositorio se despliegue correctamente:

### 1. **Dockerfile** (`docker/Dockerfile`)
- Actualización de la URL del repositorio de GitHub para apuntar al fork personal: `https://github.com/antonioluisjf22/EGC-2324-1140-antjimde.git`
- Corrección del comando `git clone` para clonar el repositorio directamente en el directorio `/app` usando el `.` como destino.

### 2. **docker-compose.yml** (`docker/docker-compose.yml`)
- Configuración de la contraseña de PostgreSQL: `POSTGRES_PASSWORD=decide`

### 3. **docker-settings.py** (`docker/docker-settings.py`)
- **HOST de base de datos**: Cambiado de `localhost` a `db` (nombre del servicio Docker Compose)
- **Puerto de base de datos**: Cambiado de `8000` a `5432` (puerto estándar de PostgreSQL)
- **CSRF_TRUSTED_ORIGINS**: Configuración de IP de la red Docker `10.5.0.1:8000`
- **BASEURL y APIS**: Actualización de todas las URLs para apuntar a `http://10.5.0.1:8000` (IP en la red Docker)

## Despliegue

### Requisitos
- Docker y Docker Compose instalados

### Pasos para desplegar

1. **Construir y levantar los servicios**
   ```bash
   cd docker
   docker-compose up --build
   ```

2. **Esperar a que los contenedores estén listos**
   - La base de datos PostgreSQL se inicializará automáticamente
   - Las migraciones de Django se ejecutarán automáticamente
   - El servidor Gunicorn se iniciará en el puerto 5000
   - Nginx actuará como proxy inverso en el puerto 8000

### Arquitectura de servicios

- **db**: Contenedor PostgreSQL (puerto interno: 5432)
- **web**: Aplicación Django con Gunicorn (puerto interno: 5000)
- **nginx**: Servidor proxy inverso (puerto externo: 8000)

## Verificar en navegador

1. **Acceder a admin:**
   - URL: `https://localhost:8000/admin`
   - Usuario: `admin`
   - Contraseña: `admin`

2. **Crear superusuario (si no existe):**
   ```bash
   docker exec -it decide_web ash
   cd /app/decide
   python manage.py shell
   ```
   
   Dentro del shell:
   ```python
   from django.contrib.auth.models import User
   User.objects.create_superuser('admin', 'admin@example.com', 'admin')
   print("Admin creado!")
   exit()
   ```

3. **Verificar que funciona:**
   - Debería ver el panel de administración de Django
   - Si aparece, Docker está desplegado correctamente ✅

4. **Logs de workers:**
   ```bash
   docker logs decide_web
   ```
   Debería ver: `Spawning worker with pid: ...` (múltiples líneas para todos los workers)

### Detener Docker

```bash
docker compose down -v
```
- `-v` para borrar volúmenes y reiniciar la base de datos

---

## Checklist de verificación

- ✅ Dockerfile apunta al repo actual (antonioluisjf22)
- ✅ Gunicorn configurado con 5 workers
- ✅ docker-compose.yml actualizado
- ✅ Admin accesible en `https://localhost:8000/admin`
- ✅ Base de datos PostgreSQL conectada correctamente
- ✅ Credenciales por defecto funcionan (usuario: admin, contraseña: admin)

## Notas técnicas

- La red Docker está configurada con subnet `10.5.0.0/16` para permitir la comunicación entre contenedores
- Los volúmenes `decide_static` y `decide_db` persisten los datos entre reinicios
- El servidor web utiliza Gunicorn con 5 workers y un timeout de 500 segundos
- Nginx actúa como proxy inverso, redirigiendo todas las peticiones al servicio web
- Los archivos estáticos se sirven directamente desde Nginx para mejor rendimiento
