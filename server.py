from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        # 如果访问根路径，重定向到main.html
        if self.path == '/':
            self.path = '/main.html'
        return SimpleHTTPRequestHandler.do_GET(self)

server_address = ('', 8000)
httpd = HTTPServer(server_address, CustomHandler)
print('启动服务器在端口 8000...')
print('请访问: http://localhost:8000')
httpd.serve_forever()