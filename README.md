# Desplegar appApi de python en apache

## Actualizar Repositorio
sudo apt update

sudo apt upgrade

## Comprobar versionde Python
python3 --version (3.10 o superior)

## Instalar Libreria WSGI de Python para Apache y activar modulo
sudo apt install libapache2-mod-wsgi-py3

sudo a2enmod wsgi

## Instalar Pip3
sudo apt install python3-pip

pip3 --version

## Instalar Flask de Manera Global
sudo pip3 install flask

## Comprobar que flask este instalado
pip3 list

### Editar sitio por defecto 000-default.conf para ejecutar app en modo Daemon
sudo nano /etc/apache2/sites-available/000-default.conf

<VirtualHost *:8080 *:8081 *:8082 *:8083 *:8084 *:8085>

        ServerAdmin webmaster@localhost

        ServerName localhost
        
        WSGIDaemonProcess proceso1 user=www-data group=www-data processes=2 threads=15 python-path=/var/www/flask/appApi:/var/www/flask/appApi/lib/python3.10/site-packages
        WSGIProcessGroup proceso1

        WSGIScriptAlias / /var/www/flask/appApi/wsgi/api.wsgi
        <Directory /var/www/flask/api472>
                Options FollowSymLinks
                AllowOverride None
                Require all granted
        </directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

NOTA: Se deben agregar los puertos que se habiliten en el archivo /etc/apache/ports.conf

## Descargar repositorio de la appApi en el home del usuario
https://github.com/nestorsramosarteaga/pythonapi

## Cambiar de propietario a la carpeta flask
sudo chown -R $USER:$USER /var/www/flask

## Crear Entorno Virtual con el mismlo nombre que appApi

cd /var/www/flask

virtualenv appApi

#sudo virtualenv -p /usr/bin/python3 appApi

## Trasladar el contenido de la carpeta src a var/www/flask/appApi

cp -r path/pythonapi/src/* /var/www/flask/appApi/

## Entrar al entorno virtual e instalar Flask, pandas y requerimientos

. appApi/bin/activate

pip3 install Flask

pip3 install pandas

pip3 install -r appApi/requirements.txt

pip3 list

## Crear .env dentro de la carpeta appApi/
SECRET_KEY=

DB_HOST=

DB_USER=

DB_PASSWORD=

DB_DATABASE=

## Reiniciar Apache
sudo systemctl restart apache2