import http.server

SERVER_ADDRES = ('', 7999)
http = http.server.HTTPServer(SERVER_ADDRES, http.server.CGIHTTPRequestHandler)
http.serve_forever()