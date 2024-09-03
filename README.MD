## crear enviroment
path: main

python3 -m venv venv

## Activar env
path: todos

activar:
source venv/bin/activate 

desactivar:
source venv/bin/deactivate

## instalacion fast api
pip install fastapi uvicorn

pip uninstall fastapi

## para recopilar todos los paquetes que estamos usando en un solo archivo:
pip freeze > requirements.txt

## isntalar todos los paquetes que se encuentran en requirements.txt

pip install -r requirements.txt

## iniciar con uvicorn el servidor dev

esto despues de crear el archivo api.py configurarlo con alguna ruta

uvicorn api:app --port 8000 --reload
