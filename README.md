## _QUICKSTART_

### for first run:

```
docker-compose up
```

#### wait for migrations to apply...

#### then load sample data:

```
docker exec -u 0 -it container_name python manage.py shell
>> from temapi.tasks import load_example_data
>> load_example_data()
```

#### then create superuser:

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
