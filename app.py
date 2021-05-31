from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)


# def creating_list():
#     print(fetch('https://jsonplaceholder.typicode.com/todos/1').then(response => response.json()).then(json => console.log(json)))

url_post = 'https://jsonplaceholder.typicode.com/posts'
resp = requests.get(url_post)
posts = resp.json()

url_post = 'https://jsonplaceholder.typicode.com/users'
resp = requests.get(url_post)
users = resp.json()

for post in posts:
    for user in users:
        if user['id'] == post['userId']:
            post['name'] = user['name']
    


@app.route('/')
def index():
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run()