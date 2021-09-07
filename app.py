from flask import Flask, render_template,request, jsonify, url_for, flash, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2 
import psycopg2.extras


app = Flask(__name__)
app.secret_key = "SkillChen_Secret_Key"

DB_HOST = "localhost"
DB_PORT = '5433'
DB_NAME = "sampledb"
DB_USER = "postgres"
DB_PASS = "dba"

conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host=DB_HOST,port=DB_PORT)


@app.route("/")
def index():
    
    hash = generate_password_hash('skillchen')
    check_hash = check_password_hash(hash ,'skillchen')
    return render_template("index.html", hash=hash, check_hash=check_hash)

@app.route("/action", methods=["POST","GET"])
def action():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        cur.execute("select * from admin_login where admin_name = %s", [username,])
        total_row = cur.rowcount
        #print(total_row)
        if total_row > 0:
            data = cur.fetchone()
            rs_password = data['admin_password']
            #print(rs_password)
            if check_password_hash(rs_password, password):
                session['logged_in'] = True
                session['username'] = username
                msg = 'success'
            else:
                msg = 'No-data'
        else:
            msg = 'No-data'                
    return jsonify(msg)

@app.route("/logout")    
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
