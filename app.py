from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    # Here you would integrate your NLP model for response generation
    bot_response = generate_bot_response(user_message)
    return jsonify({'response': bot_response})

def generate_bot_response(user_message):
    # Placeholder for the AI logic
    responses = {
        "hi": "Hello! How can I assist you today?",
        "i'm looking for a new laptop.": "Sure, do you have any specific brand in mind?",
        "i prefer dell.": "Great choice! Here are some options for Dell laptops."
    }
    return responses.get(user_message.lower(), "I'm here to help with your inquiries!")

if __name__ == "__main__":
    app.run(debug=True)