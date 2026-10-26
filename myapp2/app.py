import json
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = {
            "app": "myapp2",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode() + b"\n")

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
