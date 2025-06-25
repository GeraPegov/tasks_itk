import socket

import requests

HOST = "localhost"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Сервер запущен на http://{HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            request = conn.recv(1024).decode()
            point = request.splitlines()[0]
            try:
                path = point.split(" ")[1][1:].strip()
                api_url = f"https://api.exchangerate-api.com/v4/latest/{path}"
                response = requests.get(api_url).json()
            except IndexError:
                path = ""
            except requests.JSONDecodeError:
                path = ""
            if not path:
                response_body = "Hello"
                response = (
                    "HTTP/1.1 200\r\n"
                    "Content-Type: text/html\r\n"
                    f"Content-Length: {len(response_body)}\r\n"
                    "\r\n"
                    f"{response_body}"
                )
            else:
                response = (
                    "HTTP/1.1 200\r\n"
                    "Content-Type: application/json\r\n"
                    f"Content-Lenght: {len(response)}\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                    f"{response}"
                )
            conn.sendall(response.encode())
