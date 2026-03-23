import http.server
import os
import sys

PORT = 3000

class MoodServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/style.css':
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            with open('style.css', 'rb') as f:
                self.wfile.write(f.read())
        elif self.path == '/config.js':
            # Safely provide the API key to the frontend
            self.send_response(200)
            self.send_header('Content-type', 'application/javascript')
            self.end_headers()
            api_key = os.environ.get('GEMINI_API_KEY', '')
            content = f"window.ENV = {{ GEMINI_API_KEY: '{api_key}' }};"
            self.wfile.write(content.encode())
        else:
            super().do_GET()

if __name__ == '__main__':
    print(f"Mood Server starting on port {PORT}...")
    server = http.server.HTTPServer(('0.0.0.0', PORT), MoodServer)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        sys.exit(0)
