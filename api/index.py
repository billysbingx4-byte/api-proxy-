from flask import Flask, request
import requests

app = Flask(name)

# This handles both /api and /api/
@app.route('/api', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    url = f"https://api.telegram.org/{path}"
    resp = requests.request(
        method=request.method,
        url=url,
        headers={k: v for k, v in request.headers.items() if k.lower() != 'host'},
        data=request.get_data(),
        params=request.args
    )
    return (resp.content, resp.status_code, resp.headers.items())
