from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class mainHandler(BaseHTTPRequestHandler):
	def do_HEAD(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
	def do_GET(self):
		f = open('blog-home.html')
		if self.path=='/test.html':
			f = open('test.html')
		if self.path=='/blog-home.html':
			f = open('blog-home.html')
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(f.read())

try:
	server=HTTPServer(("",PORT_NUMBER),mainHandler)
	print('Started httpserver on port',PORT_NUMBER)
	server.serve_forever()
except KeyboardInterrupt:
	print('^C recieved, shutting down the web server')
	server.socket.close()