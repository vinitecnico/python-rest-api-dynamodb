# docker

### run

```
    docker-compose up
```

### stop

```
    docker-compose down
```


# request

### GET  - All

```
    curl --location 'http://localhost:5000/items'
```

### POST - create

```
    curl --location 'http://localhost:5000/items' \
    --header 'Content-Type: application/json' \
    --data-raw '{"id": 456, "name": "Jane Doe", "age": 25, "email": "janedoe@example.com"}'
```

### GET - by id

```
    curl --location 'http://localhost:5000/items/1'
```

### PUT - update

```
    curl --location --request PUT 'http://localhost:5000/items/1' \
    --header 'Content-Type: application/json' \
    --data-raw '{"id": 1, "name": "test silva", "age": 40, "email": "test1-silva@example.com"}'
```

### DELETE

```
    curl --location --request DELETE 'http://localhost:5000//items/2'
```