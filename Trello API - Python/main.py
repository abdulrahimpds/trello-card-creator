from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

def read_texts(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()

api = read_texts('api.txt')
token = read_texts('token.txt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        board_id = request.form['board_id']
        list_name = request.form['list_name']
        name = request.form['name']
        desc = request.form['desc']
        due = request.form['due']
        start = request.form['start']

        # Fetching the lists from the board
        url = f"https://api.trello.com/1/boards/{board_id}/lists"
        headers = {
          "Accept": "application/json"
        }
        query = {
          'key': api,
          'token': token
        }
        response = requests.request("GET", url, headers=headers, params=query)
        lists_data = json.loads(response.text)

        # Creating a dictionary with list names as keys and their respective ids as values
        list_name_to_id = {list_item['name']: list_item['id'] for list_item in lists_data}

        list_id = list_name_to_id.get(list_name, None)
        if not list_id:
            return f"List with the name {list_name} not found."
            return redirect(url_for('index'))

        url = "https://api.trello.com/1/cards"
        query = {
            'name': name,
            'desc': desc,
            'due': due,
            'start': start,
            'idList': list_id,
            'key': api,
            'token': token
        }

        response = requests.request("POST", url, headers=headers, params=query)

        # Check the response
        if response.status_code == 200:
            return "Card created successfully!"
        else:
            return "Failed to create the card."
        
        return redirect(url_for('index'))

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
