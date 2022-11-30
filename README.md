# backend

## Requisitos de desarrollo
  * Python 3.9
  * Docker
  * Docker Compose

## Requisitos para deployment
  * aws-cli
  * docker-cli
  * docker-compose-plugin

## Preparación del entorno

### Fichero .env

Antes de nada tenemos que crear un fichero .env en la raíz del proyecto.
Hay un .env de ejemplo llamado **.env.example**, solo tenemos que rellenar los
datos de ese fichero y renombrarlo como .env

Este fichero es el que nos va a permitir tener diferentes entornos, local, stage
y producción. No se sube al repositorio se debe crear cuando hacemos el deploy
del código en cada entorno.

### Unix

    $ python -m venv .venv/novahack
    $ source .venv/novahack/bin/activate
    $ pip install -r requirements.txt
    $ pip install -r requirements_dev.txt
    $ ./scripts/init.sh

### Windows

    $ python -m venv .venv/novahack
    $ .venv/novahack/bin/activate.bat
    $ pip install -r requirements.txt
    $ pip install -r requirements_dev.txt

  Levantar la bbdd y esperar a que este totalmente levantada e inicializada:

    $ docker-compose up db

  Configurar Django:

    $ docker-compose run --rm api python manage.py migrate
    $ docker-compose run --rm api python manage.py createsuperuser
## Scripts

Se encuentran en el directorio de scripts y son los siguientes:

  - **init.sh:** Inicializa todo el entorno de desarrollo en un sistema unix
  - **manage.sh args:** Ejecuta el comando python manage.py {args} en el
    servicio api

## Iniciar backend

### Iniciar bbdd

    $ docker-compose up db

### Iniciar API

    $ docker-compose up api

## Test

Para correr los test de la API solo hay que levantar el docker api-test

    $ docker-compose -f docker-compose-test.yml up api-test

O corriendo el script:

    ./scripts/test.sh

### Test en vscode

Para ejecutar los test en vscode tendras que cambiar en las configuraciónes de
Workspace la configuración Python: Env File y cambiarlo para que no sea el
fichero .env

## Subida a Producción

### Subida de la imagen de la API

Primero debemos tener la imagen del contenedor de la API subida a ECR. Si no
tenemos nigún repositorio de imagenes el primer paso es crearlo:

    $ aws ecr create-repository --repository-name novahack_api --region eu-central-1 --profile novahack

Una vez tengamos el repositorio de imagenes docker procedemos a la subida, para
ello solo debemos ejecutar el __tag_api_image.sh__ pasandole por argumento el
tag para la imagen. De esta forma podemos tener una versión de arquitectura para
cada versión de código

    $ ./scripts/tag_api_image.sh 1.0.0

Esta imagen es la que usaremos en el docker_file para el servicio api
