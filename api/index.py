from http.server import BaseHTTPRequestHandler
import urllib.parse
import json

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):

        query_params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()

        self.wfile.write("hello")

        return 