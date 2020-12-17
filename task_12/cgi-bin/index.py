import cgi, html
r = cgi.FieldStorage()

login = html.escape(r.getvalue("login", "")).strip()
password = html.escape(r.getvalue("password", "")).strip()

flag = True
maessage = ''

if login == '' and password == '':
    maessage = ''
elif login != 'Admin' and password != '123':
    maessage = "<p style='color: red;'>Неверные логин и/или пароль</p>"
else:
    flag = False
    maessage = "<p style='color: green;'> Здравствуйте " + login + "!<p>"


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