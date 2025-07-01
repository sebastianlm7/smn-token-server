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
        
        # Guardar los primeros 1000 caracteres para debug
        snippet = html[:1000]
        
        match = re.search(r"setItem\('token', '([^']+)'", html)
        token = match.group(1) if match else None
        
        if token:
            return token
        else:
            return f"NO_TOKEN. HTML snippet:\n{snippet}"
    except Exception as e:
        return f"ERROR: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
