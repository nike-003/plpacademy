from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Sample jokes database
jokes = [
    "Why don't scientists trust atoms? Because they are made up of everything!",
    "Why did the computer go to therapy? It had too many bytes!",
    "Why do programmers prefer dark mode? Because the light attracts bugs!",
    "Why did the student eat his homework? Because the teacher said it's a piece of cake!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't eggs tell jokes? They'd crack each other up!"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_joke')
def get_joke():
    joke = random.choice(jokes)
    return jsonify({'joke': joke})

@app.route('/add_joke', methods=['POST'])
def add_joke():
    data = request.get_json()
    new_joke = data.get('joke', '').strip()
    if new_joke:
        jokes.append(new_joke)
        return jsonify({'success': True, 'message': 'Joke added successfully!'})
    return jsonify({'success': False, 'message': 'Please enter a valid joke!'})

@app.route('/all_jokes')
def all_jokes():
    return jsonify({'jokes': jokes})

if __name__ == '__main__':
    app.run(debug=True) 