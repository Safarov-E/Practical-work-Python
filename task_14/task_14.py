import http.server

SERVER_ADDRES = ('', 3000)
http = http.server.HTTPServer(SERVER_ADDRES, http.server.CGIHTTPRequestHandler)
http.serve_forever()