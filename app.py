from flask import Flask, request, jsonify
from services.item_service import ItemService

app = Flask(__name__)
item_service = ItemService()


@app.route('/items', methods=['GET'])
def get_items():
    items = item_service.get_all()
    return items


@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = item_service.get_by_id(int(item_id))
    if item:
        return item
    return jsonify({'error': 'Item not found'}), 404


@app.route('/items', methods=['POST'])
def create_item():
    item_service.create(request.get_json())
    return jsonify({'message': 'Item created successfully'}), 201

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    item_service.update(int(item_id), request.get_json())
    return jsonify({'message': 'Item updated successfully'})


@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    item_service.delete(int(item_id))
    return jsonify({'message': 'Item deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
