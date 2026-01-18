# Ejercicio D - Cambios en Vagrant

## Intensificación Colaborativa

### 1. Cambios realizados en archivos de Vagrant

Se han realizado modificaciones en los siguientes archivos para desplegar correctamente el repositorio:

#### `vagrant/user.yml`
- **Cambio**: Usuario actualizado de `decide` a `adminexamen`
- **Razón**: El usuario administrador del sistema debe ser `adminexamen`

#### `vagrant/django.yml`
- **Cambios**:
  - Usuario de ejecución: `decide` → `adminexamen`
  - Rutas de proyecto: `/home/decide/` → `/home/adminexamen/`
  - Usuario superadmin: `admin` → `adminexamen`
- **Razón**: Coherencia con el usuario del sistema

#### `vagrant/Vagrantfile`
- **Cambios**:
  - Memoria: 512 MB → 4096 MB (4 GB)
  - CPUs: 1 → 4
- **Razón**: Recursos necesarios para desplegar DECIDE correctamente

### 2. Commit de cambios

```bash
git add vagrant/user.yml vagrant/django.yml vagrant/Vagrantfile
git commit -m "Cambios en Vagrant: usuario adminexamen y 4 CPUs/4GB RAM"
git push origin vagrant
```

**Commit**: `6766f15`

## Balance Técnico-Organizativo

### 3. Rama vagrant creada y modificaciones completadas

La rama `vagrant` contiene todos los cambios necesarios para desplegar el repositorio con Vagrant.

### 4. Playbook Ansible actualizado

El playbook de Ansible ha sido modificado para crear el usuario `adminexamen` y realizar las tareas de provisioning con este usuario.

### 5. Commit y push completados

Los cambios han sido commitados y pusheados a la rama `vagrant`.

### 6. Vagrant configurado con 4 CPUs y 4 GB RAM

El Vagrantfile ha sido actualizado para utilizar los recursos especificados.

### 7. Commit y push completados

Los cambios han sido commitados y pusheados a la rama `vagrant`.

## Rebase en egc_test

La rama `egc_test` ha sido actualizada mediante rebase para incluir los cambios de la rama `vagrant`:

```bash
git checkout egc_test
git rebase vagrant
git push origin egc_test
```

La rama `egc_test` ahora contiene todos los cambios de Vagrant y está lista para el apartado 12 del Ejercicio A.
