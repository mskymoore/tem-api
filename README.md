## _QUICKSTART_

### for first run:

```
docker-compose up db tem-api nginx redis
```

#### wait for migrations to apply...

#### then load sample data:

```
docker-compose up celery
```

#### then create superuser:

```
docker exec -u 0 -it localhost python manage.py createsuperuser
```

### After first run setup, to start:

```
docker-compose up
```

### After first run setup, to stop:

```
docker-compose down
```

### To clear databases and start over:

```
docker-compose down -v
```
