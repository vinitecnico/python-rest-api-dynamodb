import os
from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

os.environ['AWS_ACCESS_KEY_ID'] = 'test'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'

dynamodb = boto3.client('dynamodb', region_name='us-east-1', endpoint_url='http://localhost:4566')
table_name = 'MyTable'

# table = dynamodb.create_table(
#     TableName=table_name,
#     KeySchema=[
#         {
#             'AttributeName': 'id',
#             'KeyType': 'HASH'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'id',
#             'AttributeType': 'N'
#         }
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

@app.route('/items', methods=['GET'])
def get_items():
    response = dynamodb.scan(TableName=table_name)

    items = []
    for item in response['Items']:
        converted_item = {}
        for key, value in item.items():
            data_type = next(iter(value))
            converted_item[key] = value[data_type]
        items.append(converted_item)

    return jsonify(items)

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    response = dynamodb.get_item(TableName=table_name, Key={'id': {'N': item_id}})
    item = response.get('Item')
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def create_item():
    item = {}

    for key, value in request.get_json().items():
        if isinstance(value, int):
            item[key] = {'N': str(value)}
        else:
            item[key] = {'S': value}

    # PutItem request with the correct Item format
    response = dynamodb.put_item(
        TableName=table_name,
        Item=item
    )
    print(response)
    return jsonify({'message': 'Item created successfully'})

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    item = request.get_json()
    item['id'] = {'N': item_id}
    response = dynamodb.put_item(TableName=table_name, Item=item)
    return jsonify({'message': 'Item updated successfully'})

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    response = dynamodb.delete_item(TableName=table_name, Key={'id': {'N': item_id}})
    return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)