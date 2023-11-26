import os
import boto3

class DynamoDBConnection:
    def __init__(self, table_name):
        os.environ['AWS_ACCESS_KEY_ID'] = 'test'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
        self.table_name = table_name
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url='http://localhost:4566')
        self.table = self.dynamodb.Table(table_name)
        
        if not self._table_exists():
            self._create_table()
    
    def _table_exists(self):
        existing_tables = self.dynamodb.meta.client.list_tables()['TableNames']
        return self.table_name in existing_tables

    
    def _create_table(self):
        table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        table.wait_until_exists()

    def get_all(self):
        response = self.table.scan(TableName=self.table_name)
        return response.get('Items', [])
    
    def get_item(self, key):
        response = self.table.get_item(Key=key)
        item = response.get('Item')
        return item
    
    def put_item(self, item):
        response = self.table.put_item(Item=item)
        return response
    
    def update_item(self, key, update_expression, expression_attribute_values, expression_attribute_names=None):
        response = self.table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames=expression_attribute_names
        )
        return response
    
    def delete_item(self, key):
        response = self.table.delete_item(Key=key)
        return response