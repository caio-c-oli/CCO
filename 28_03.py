from flask import Flask, jsonify
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1, 
        'name': "task1",
        'description': "This is task1"
    },
    {
        'id': 2, 
        'name': "task2",
        'description': "This is task2"
    },
    {
        'id': 3, 
        'name': "task3",
        'description': "This is task3"
    }
]

tasksJSON = json.dumps (tasks)

@app.route('/')
def home():
    return jsonify(texto="Texto Aleatório")

@app.route('/api/tasks')
def tasks():
    return tasksJSON

if __name__ == "__main__":
    app.run()