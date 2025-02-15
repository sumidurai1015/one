from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data
items = [
    {"id": 1, "name": "Item 1", "price": 100},
    {"id": 2, "name": "Item 2", "price": 200}
]

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    new_item = {
        "id": len(items) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    items.append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json
    item["name"] = data.get("name", item["name"])
    item["price"] = data.get("price", item["price"])
    
    return jsonify(item)

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

