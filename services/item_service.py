from services.dynamodb_connection import DynamoDBConnection

class ItemService:
    def __init__(self):
        self.dynamodb_conn = DynamoDBConnection('my_table')

    def get_all(self):
        return self.dynamodb_conn.get_all()

    def get_by_id(self, id):
        return self.dynamodb_conn.get_item({'id': id})

    def create(self, request_item):
        self.dynamodb_conn.put_item(request_item)

    def update(self, id, request_item):
        update_expression = 'SET #attr_name = :name, age = :age, email = :email'
        expression_attribute_values = {
            ':name': request_item.get('name'),
            ':age': int(request_item.get('age')),
            ':email': request_item.get('email')
        }
        expression_attribute_names = {
            '#attr_name': 'name'
        }

        self.dynamodb_conn.update_item({'id': id}, update_expression, expression_attribute_values, expression_attribute_names)

    def delete(self, id):
        self.dynamodb_conn.delete_item({'id':  id})
