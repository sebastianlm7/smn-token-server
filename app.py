from flask import Flask
import requests
import re
import os

app = Flask(__name__)

@app.route("/token")
def get_token():
    try:
        response = requests.get(
            'https://smn.gob.ar',
            headers={"Host": "smn.gob.ar"},
            verify=False
        )
        html = response.text
        match = re.search(r"setItem\('token', '([^']+)'", html)
        token = match.group(1) if match else "NO_TOKEN"
        return token
    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
