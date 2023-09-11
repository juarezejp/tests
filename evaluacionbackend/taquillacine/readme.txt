Quiero explicar por qué decidí utilizar Python en lugar de Java para desarrollar la aplicación.
al tener ya configurado el entorno de desarrollo para python, por cuestiones de tiempo para configurar 
y preparar el entorno de desarrollo para Java (descargar el JDK, IDE,y la configuración de dependencias), 
con un calendario apretado y una fecha  límite para entregar la aplicación, me vi en la necesidad de tomar 
una decisión rápida para avanzar con el desarrollo.


instrucciones para correr la aplicación 
en terminal ubicarse en los archivos dockerfile y docker-compose, ejecutar los siguientes comandos:
docker compose up -d
docker compose exec app bash
cd taquilla/
python manage.py makemigrations
python manage.py migrate
python3 manage.py runserver 0:8000
http://localhost:8000


