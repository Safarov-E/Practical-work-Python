import cgi, http.cookies, html, hashlib, os
r = cgi.FieldStorage()

login = html.escape(r.getvalue("login", "")).strip()
password = html.escape(r.getvalue("password", "")).strip()

flag = True
maessage = ''
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

if login == '' and password == '':
    maessage = ''
elif login != 'Admin' or password != '123':
    maessage = "<p style='color: red;'>Неверные логин и/или пароль</p>"

if login == 'Admin' and password == '123':
    flag = False
    print("Set-cookie: login="+login)
    print("Set-cookie: password="+ hashlib.md5(password.encode()).hexdigest())
    maessage = "<p style='color: green;'> Здравствуйте " + login + "!<p>" + "<a href='?logout=1'>Выйти</a>"
elif cookie.get('login').value == 'Admin' or cookie.get('password').value == hashlib.md5('123'.encode()).hexdigest():
    flag = False
    maessage = "<p style='color: green;'> Здравствуйте " + cookie.get('login').value + "!<p>" + "<a href='?logout=1'>Выйти</a>"
else:
    flag = True

if r.getvalue('logout') == '1':
    flag = True
    maessage = ''
    print("Set-cookie: login="+'')
    print("Set-cookie: password="+'')

print("Content-type: text/html; charset='utf-8'")
print()
print("<html><head><title>Авторизация</title></head><body style='text-align: center;'>")
if flag:
    print('''<form name="form" action="/cgi-bin/index.py" method="POST">
        <h2>Авторизация</h2>
        ''' + maessage + '''
        <p>Логин: <input type="text" name="login" value="'''+ login + '''"/></p>
        <p>Пароль: <input type="text" name="password" value="''' + password + '''"/></p>
        <input type="submit" value="Войти" />
    </form>''')
else:
    print(maessage)
print("</body></html>")