from flask import Flask,render_template,request
import mysql.connector



app= Flask(__name__)

conn=mysql.connector.connect(host="remotemysql.com",user="9YwiYaINDg",password="WB2u9rVHb5",database="9YwiYaINDg")
cursor=conn.cursor()



@app.route('/',methods=['GET', 'POST'])
def index():
     return render_template('login.html')










@app.route("/loginvalidation", methods=['POST'])
def loginval():
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
    print(users)
    # dic={}
    # dic[users[0][1]]=users[0][2]
    # return dic
    return users



















if __name__ == '__main__':
    app.run(debug=True)