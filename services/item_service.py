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

    def delete(self, id):
        self.dynamodb_conn.delete_item({'id':  id})
