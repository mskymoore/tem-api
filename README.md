## _QUICKSTART_

### for first run:

```
docker-compose up db redis tem-api nginx
```

#### wait for migrations to apply...

```
# press ctrl + \ to drop from the docker-compose output
docker-compose up
```

#### then load sample data:

```
docker exec -u 0 -it container_name python manage.py shell
>> from temapi.tasks import load_example_data
>> load_example_data()
```

#### then create superuser if additional desired:

```
docker exec -u 0 -it localhost python manage.py createsuperuser
```

### To start:

```
docker-compose up
```

### To stop:

```
docker-compose down
```

### To clear databases and start over:

```
docker-compose down -v
```
