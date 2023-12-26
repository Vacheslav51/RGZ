from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
import psycopg2
from flask_login import login_user, login_required, current_user, logout_user

menu = Blueprint('menu', __name__)

@menu.route('/menu/')
def main():
    return render_template('menu.html')



def con():
    conn = psycopg2.connect(
        host = "127.0.0.1",
        database = "Mes",
        user = "gri",
        password = "1226"
    )
    return conn;

def close(cursor , connection):
    cursor.close()
    connection.close()

@menu.route('/users')
def user():
    conn = con()
    cur = conn.cursor()

    cur.execute("SELECT name FROM users;")

    result = cur.fetchall()
    result = result

    close(cur, conn)

    return render_template('users.html', result = result)


@menu.route('/reg/', methods=["GET", "POST"])
def reg():
    errors = []

    if request.method == "GET":
        return render_template("reg.html", errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username or password):
        errors.append('Заполните все поля!')
        print(errors)
        return render_template("reg.html", errors=errors)
    
    hashPassword = generate_password_hash(password)

    conn = con()
    cur = conn.cursor()

    cur.execute(f"SELECT name FROM users WHERE name = '{username}';")

    if cur.fetchone() is not None:
        errors.append("Такой пользователь уже есть")
        close(cur, conn)
        return render_template("reg.html", errors=errors)
    
    cur.execute(f"INSERT INTO users ( name,password) VALUES ('{username}','{hashPassword}');")
    
    conn.commit()
    close(cur, conn)

    return redirect('/menu/login')

@menu.route("/menu/login", methods=['GET','POST'])
def loginPage():
    errors = []
    if request.method == "GET":
        return render_template("login.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")
    
    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        return render_template("login.html", errors=errors)
    
   
    conn = con()
    cur = conn.cursor()

    cur.execute(f"select id, password from users where name = '{username}'")

    result=cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        close(cur,conn)
        return render_template("login.html", errors=errors)
    
    userID, hashPassword,= result

   
    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['name'] = username
        close(cur, conn)
        return redirect("/menu/chat")
    else:
        errors.append("Неправильный пароль или логин")
        return render_template("login.html", errors=errors)
    

@menu.route('/menu/chat', methods=['GET','POST'])
def chat():
    userID = session.get("id")
    name_p = request.form.get("'name_p'")
    conn = con()
    cur = conn.cursor()


    if name_p is None:

        cur.execute(f"SELECT users.name FROM messages JOIN users ON messages.pysh_id = users.id WHERE  on_id = {userID} ;")

        name = cur.fetchall()
        name_full = name

        cur.execute(f"SELECT messages.text FROM messages JOIN users ON messages.pysh_id = users.id WHERE  on_id = {userID};")
        
        text = cur.fetchall()

        cur.execute(f"SELECT messages.text FROM messages JOIN users ON messages.pysh_id = users.id WHERE  pysh_id = {userID};")
        
        text_me = cur.fetchall()

        cur.execute(f"SELECT users.name FROM messages JOIN users ON messages.pysh_id = users.id WHERE  pysh_id = {userID};")
        
        text_me_name = cur.fetchall()


        conn.commit()
        close(conn, cur)
        return render_template("chat.html", name_full=name_full, text=text, text_me=text_me, text_me_name=text_me_name)

    
    else:
        return redirect("/menu/chat")


@menu.route('/menu/sms',  methods=["GET", "POST"])
def sms():
    errors = []

    if request.method == "GET":
        return render_template("sms.html", errors=errors)

    text_p = request.form.get('text_p')
    
    name_p = request.form.get("name_p")

    userID = session.get("id")

    if not (text_p or name_p):
        errors.append('Заполните все поля!')
        print(errors)
        return render_template("sms.html", errors=errors)
    

    conn = con()
    cur = conn.cursor()

    cur.execute(f"select id from users where name = '{name_p}'")
    p = cur.fetchall()
    y = [x[0] for x in p]

    cur.execute(f"INSERT INTO messages (text, pysh_id, on_id) VALUES ({text_p }, {userID}, {y});")
    
    conn.commit()
    close(cur, conn)

    return redirect('/menu/chat')
    
@menu.route('/users',  methods=["GET", "POST"])
def dell():
    userID = session.get("id")
    if request.method == "GET" and userID == '1':
        errors =  'Такого пользователя нет'
        return render_template("users.html", errors=errors)

    des = request.form.get('des')

    conn = con()
    cur = conn.cursor()

    

    cur.execute(f"DELETE FROM users WHERE name = {des};")
    
    conn.commit()
    close(cur, conn)

    return redirect('/menu')

    
    


