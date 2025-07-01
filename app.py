from flask import Flask
import requests
import re

app = Flask(__name__)

@app.route("/token")
def get_token():
    html = requests.get(
        'https://smn.gob.ar',
        headers={"Host": "smn.gob.ar"},
        verify=False
    ).text
    match = re.search(r"setItem\('token', '([^']+)'", html)
    return match.group(1) if match else "NO_TOKEN"
