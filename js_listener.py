from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote

with open("loga.txt","w") as f:
			f.write('')
class RequestHandler(BaseHTTPRequestHandler):
	def _set_response(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		with open("loga.txt","a") as f:
			f.write(str(self.path)[1:])
		self._set_response()
	def do_POST(self):
		with open("loga.txt","a") as f:
			f.write(str(self.path)[1:])
		self._set_response()

def run():
   	print('starting server...')
   	server_address = ('127.0.0.1', 5555)
   	httpd = HTTPServer(server_address, RequestHandler)
   	try:
   		httpd.serve_forever()
   	except KeyboardInterrupt:
   		with open("loga.txt","r") as f:
   			url = f.readlines()[0]
   			url = unquote(url)
   		with open("loga.txt","w") as f:
   			f.write(url)
   		pass
   	httpd.server_close()
run()