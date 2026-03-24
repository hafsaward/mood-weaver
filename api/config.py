from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/javascript')
        self.end_headers()
        # Vercel will provide this from the Environment Variables you set in the dashboard
        api_key = os.environ.get('GEMINI_API_KEY', '')
        content = f"window.ENV = {{ GEMINI_API_KEY: '{api_key}' }};"
        self.wfile.write(content.encode())
        return
