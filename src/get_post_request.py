from http.server import BaseHTTPRequestHandler, HTTPServer


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс, описывающий работу сервера. Дочерний класс класса BaseHTTPRequestHandler."""

    def do_GET(self):
        """Метод, обрабатывающий GET запросы."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("../html/contacts.html", encoding="utf-8") as file:
            content = file.read()
        self.wfile.write(bytes("{'message': 'OK'}", "utf-8"))

    def do_POST(self):
        """Метод, обрабатывающий POST запросы."""
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")