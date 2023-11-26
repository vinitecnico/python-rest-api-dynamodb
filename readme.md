docker-compose up
docker-compose down

GET  - All
curl --location 'http://localhost:5000/items'

POST - create
curl --location 'http://localhost:5000/items' \
--header 'Content-Type: application/json' \
--data-raw '{"id": 456, "name": "Jane Doe", "age": 25, "email": "janedoe@example.com"}'