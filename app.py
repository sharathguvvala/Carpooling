from flask import Flask,render_template,request,redirect,session
import mysql.connector
import os


app= Flask(__name__)
app.secret_key=os.urandom(24)
 
conn=mysql.connector.connect(host="remotemysql.com",user="9YwiYaINDg",password="WB2u9rVHb5",database="9YwiYaINDg")
cursor=conn.cursor()



@app.route('/',methods=['GET', 'POST'])
def index():
     return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')
   

@app.route("/loginvalidation", methods=['POST'])
def loginval():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        session['user_id']=users[0][0]
        return redirect('/home')
    else:
        return redirect('/login')


    # dic={}
    # dic[users[0][1]]=users[0][2]
    # return dic
    


@app.route('/add_user',methods=['POST'])
def add_user():
    name=request.form.get('username')
    email=request.form.get('useremail')
    password=request.form.get('userpassword')
    phone_number=request.form.get('userphone')

    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`,`phone_number`) VALUES (NULL,'{}','{}','{}','{}')""".format(name,email,password,phone_number))
    conn.commit()
    return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')












if __name__ == '__main__':
    app.run(debug=True)

