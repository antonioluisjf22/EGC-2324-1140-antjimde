# Ejercicio B - GitHub Actions

## Intensificación Colaborativa

### 1. Workflow django.yml - Tests sin cobertura

Se modificó el workflow `django.yml` para ejecutar las pruebas sin análisis de cobertura ni integración con Codacy:

- **Cambio**: Eliminado `coverage run --branch --source=.` 
- **Comando final**: `python manage.py test --keepdb`
- **Resultado**: Tests ejecutados de forma simple y directa sin reportes de cobertura

### 2. Ejecución solo en rama egc_test

El workflow se configuró para ejecutarse únicamente en la rama `egc_test`:

```yaml
on:
  push:
    branches:
      - egc_test
```

Esto garantiza que el CI solo se ejecute en la rama de testing especificada.

### 3. Commit y push

```bash
git add .github/workflows/django.yml
git commit -m "Ejercicio B: Configurar workflows - egc_test solo, PostgreSQL 14.9 y 15.6, sin cobertura"
git push origin egc_test
```

### 4. Verificación del workflow

El workflow se ejecuta automáticamente al hacer push en la rama `egc_test` con dos jobs paralelos para validar la compatibilidad con diferentes versiones de PostgreSQL.

## Balance Técnico-Organizativo

### 5. PostgreSQL multi-versión

Se configuraron dos jobs independientes para probar con diferentes versiones de PostgreSQL:

- **Job 1 - `build-postgres-14`**: PostgreSQL 14.9
- **Job 2 - `build-postgres-15`**: PostgreSQL 15.6

Esta estrategia permite detectar problemas de compatibilidad entre versiones sin duplicar lógica.

```yaml
jobs:
  build-postgres-14:
    services:
      postgres:
        image: postgres:14.9
  
  build-postgres-15:
    services:
      postgres:
        image: postgres:15.6
```

### 6. Commit y push

Los cambios fueron commitados y pusheados correctamente a la rama `egc_test`.

### 7. Verificación del workflow

El workflow se ejecuta exitosamente con ambas versiones de PostgreSQL, validando que DECIDE funciona correctamente en ambos entornos.

## Intensificación Técnica

### 8. Releases automáticas

Se creó el workflow `release.yml` que genera releases automáticas en la rama `main`:

```yaml
on:
  push:
    branches:
      - main
```

**Funcionalidad:**
- Genera un tag con versión `v1.0.{commit_count}`
- Crea una release en GitHub automáticamente
- Se dispara en cada push a `main`

### 9. Commit y push

El workflow fue commitado y pusheado en la rama principal.

### 10. Verificación de releases

Las releases se generan automáticamente cuando se realiza push a `main`, con tags y metadatos incluidos en la release.

## Resumen de Cambios

| Aspecto | Cambio |
|--------|--------|
| Cobertura | ❌ Eliminada |
| Codacy | ❌ Eliminada |
| Rama de ejecución | Solo `egc_test` |
| PostgreSQL | 14.9 y 15.6 (2 jobs) |
| Releases automáticas | ✅ Habilitadas en `main` |
| Versionado | `v1.0.{commit_count}` |

Todos los apartados del Ejercicio B han sido completados exitosamente.
