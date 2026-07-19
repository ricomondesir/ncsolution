#Migration
python manage.py makemigrations
python manage.py migrate

# create super user
python manage.py createsuperuser
Username (leave blank to use 'teklib'): rico
Email address: rico@hitmosa.com
Password: @12345

pip install dj-database-url
pip freeze > requirements.txt

python manage.py test -v 2

## list of all containers
    sudo docker ps -a
    sudo docker container ls -a

    ### remove container
    sudo docker rm container_id 

    ### remove image
    sudo docker rmi image_id 

## Create and start containers  (in the background -d or --detach)
    sudo docker-compose up -d

## Stop services
    sudo docker-compose stop