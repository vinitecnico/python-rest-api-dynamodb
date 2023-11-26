from flask import Flask, request, jsonify
from services.item_service import ItemService

app = Flask(__name__)
item_service = ItemService()

@app.route('/items', methods=['GET'])
def get_items():
    items = item_service.get_all()
    return jsonify(items)

# @app.route('/items/<item_id>', methods=['GET'])
# def get_item(item_id):
#     response = dynamodb.get_item(TableName=table_name, Key={'id': {'N': item_id}})
#     item = response.get('Item')
#     if item:
#         return jsonify(item)
#     return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def create_item():
    item_service.create(request.get_json())
    return jsonify({'message': 'Item created successfully'})

# @app.route('/items/<item_id>', methods=['PUT'])
# def update_item(item_id):
#     item = request.get_json()
#     item['id'] = {'N': item_id}
#     response = dynamodb.put_item(TableName=table_name, Item=item)
#     return jsonify({'message': 'Item updated successfully'})

# @app.route('/items/<item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     response = dynamodb.delete_item(TableName=table_name, Key={'id': {'N': item_id}})
#     return jsonify({'message': 'Item deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)