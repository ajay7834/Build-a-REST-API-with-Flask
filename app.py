from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user data (dictionary)
users = {}

# Home Route
@app.route('/')
def home():
    return "Welcome to the User Management REST API!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a single user by ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({user_id: user})
    return jsonify({"error": "User not found"}), 404

# POST - Add new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = str(data.get('id'))
    name = data.get('name')
    email = data.get('email')

    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = {"name": name, "email": email}
    return jsonify({"message": "User added successfully!"}), 201

# PUT - Update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated successfully!"})

# DELETE - Remove user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted successfully!"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)