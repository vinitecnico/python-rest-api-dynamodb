from services.dynamodb_connection import DynamoDBConnection

class ItemService:
    def __init__(self):
        self.dynamodb_conn = DynamoDBConnection('my_table')

    
    def get_all(self):
        return self.dynamodb_conn.get_all()


    def create(self, request_item):
        self.dynamodb_conn.put_item(request_item)