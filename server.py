from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class CustomHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/':
      self.path = '/public/index.html'

    try:
      file_path = os.getcwd() + self.path

      if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
          self.send_response(200)
          self.send_header('Content-Type','text/html')
          self.end_headers()
          self.wfile.write(file.read())
      else:
        self.send_error(404,"File Not Found")

    except Exception as e:
      self.send_error(500,f"server Error: {str(e)}")

def run(server_class=HTTPServer, handler_class=CustomHandler, port = 8080):
  server_address = ('',port)
  httpd = server_class(server_address, handler_class)
  print(f"Starting server on port {port}...")
  httpd.serve_forever()

if __name__ == "__main__":
  run()
