from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

def process_data(data):
    numbers = []
    alphabets = []
    highest_lowercase = None

    for item in data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)
            if item.islower():
                if highest_lowercase is None or item > highest_lowercase:
                    highest_lowercase = item

    return numbers, alphabets, highest_lowercase

# POST method to handle JSON input
@app.route('/bfhl', methods=['POST'])
def process_input():
    try:
        # Parse JSON data from request
        input_data = request.get_json()
        data = input_data.get('data', [])

        # Process data
        numbers, alphabets, highest_lowercase = process_data(data)

        # Create response
        response = {
            "is_success": True,
            "user_id": "shreyas_rb_26032003",  
            "email": "jshreyas.rb2021@vitstudent.ac.in",         
            "roll_number": "21BAI1220",        
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle exceptions and return failure response
        return jsonify({"is_success": False, "message": str(e)}), 400

# GET method to return operation code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
