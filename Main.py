from flask import Flask,  session, send_file, render_template,  request
from werkzeug.utils import secure_filename
import datetime
import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


conn = mysql.connector.connect(user='root', password='', host='localhost', database='1CollegeAsspy')

@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/StudentLogin")
def StudentLogin():
    return render_template('StudentLogin.html')


@app.route("/AdminAssign")
def AdminAssign():
    return render_template('AdminAssign.html')


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            return render_template('AdminHome.html')

        else:
            error="Incorrect Username or Password"
            return render_template('index.html', error=error)

@app.route("/admin")
def admin():
    return render_template("AdminHome.html")

@app.route("/NewStudent1", methods=['GET', 'POST'])
def NewStudent1():
    if request.method == 'POST':
        regno = request.form['regno']
        name = request.form['name']
        gender = request.form['gender']
        Age = request.form['Age']
        email = request.form['email']
        pnumber = request.form['pnumber']
        address = request.form['address']
        Degree = request.form['degree']
        depart = request.form['dept']
        year1 = request.form['year1']
        cursor = conn.cursor()
        cursor.execute(
            "insert into regtb values('" + regno + "','" + name + "','" + gender + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + Degree + "','" + depart + "','" + year1 + "')")
        conn.commit()
        conn.close()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminStudentInfo.html', data=data)


@app.route("/AdminStudentInfo")
def AdminStudentInfo():
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminStudentInfo.html', data=data)


@app.route("/AdminAssignInfo")
def AdminAssignInfo():
    cur = conn.cursor()
    cur.execute("SELECT * FROM assigntb")
    data = cur.fetchall()
    return render_template('AdminAssignInfo.html', data=data)


@app.route("/NewAssign", methods=['GET', 'POST'])
def NewExam1():
    if request.method == 'POST':
        exname = request.form['exname']
        subname = request.form['subname']
        date = request.form['date']
        Degree = request.form['Degree']
        depart = request.form['dept']
        year1 = request.form['year1']
        cdate = datetime.datetime.now().strftime("%d-%m-%Y")
        cursor = conn.cursor()
        cursor.execute(
            "select *  from regtb where Degree='" + Degree + "' and Department='" + depart + "' and  Year='" + year1 + "' ")
        data = cursor.fetchall()
        for i in data:
            regno = i[0]
            cursor = conn.cursor()
            cursor.execute(
                "insert into assigntb values('','" + exname + "','" + subname + "','" + date + "','" + Degree + "','" + depart + "','" + year1 + "','" + cdate + "','" + regno + "','','NotUpload')")
            conn.commit()
            conn.close()

    cur = conn.cursor()
    cur.execute("SELECT * FROM assigntb")
    data = cur.fetchall()
    return render_template('AdminAssignInfo.html', data=data)


@app.route("/studentlogin", methods=['GET', 'POST'])
def studentlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['regno'] = request.form['uname']

        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where regno='" + username + "' and Phone='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            error="Incorrect Username or Password"
            return render_template('index.html',error=error)
        else:
            print(data[0])
            session['uid'] = data[0]
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where regno='" + username + "' and Phone='" + password + "'")
            data = cur.fetchall()

            return render_template('StudentHome.html', data=data)

@app.route("/student")
def Student1():
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where regno='" + session['regno']+"'")
    data = cur.fetchall()
    return render_template('StudentHome.html', data=data)

@app.route("/StudentAssignmentInfo")
def StudentAssignmentInfo():
    cur = conn.cursor()
    cur.execute("SELECT * FROM assigntb where regno='" + session['regno'] + "' and AssFile ='' ")
    data = cur.fetchall()
    return render_template('StudentAssignmentInfo.html', data=data)


@app.route("/StudentUploadInfo")
def StudentUploadInfo():
    cur = conn.cursor()
    cur.execute("SELECT * FROM assigntb where regno='" + session['regno'] + "' and AssFile!='' ")
    data = cur.fetchall()
    return render_template('StudentUploadInfo.html', data=data)


@app.route("/uploadassign", methods=['GET', 'POST'])
def uploadassign():
    if request.method == 'POST':
        id = request.form['id']
        file = request.files['fileupload']
        file.save("static/upload/" + secure_filename(file.filename))

        print(id)

        cursor = conn.cursor()
        cursor.execute(
            "update assigntb set status='upload',AssFile='" + file.filename + "' where id='" + str(id) + "' ")
        conn.commit()
        conn.close()

        cur = conn.cursor()
        cur.execute("SELECT * FROM assigntb where regno='" + session['regno'] + "' and AssFile!='' ")
        data = cur.fetchall()
        return render_template('StudentUploadInfo.html', data=data)

@app.route("/down")
def down():
    id = request.args.get('lid')
    print(id)

    cursor = conn.cursor()
    cursor.execute("SELECT * from assigntb where id ='" + id + "' and Assfile !=''  ")
    data = cursor.fetchone()
    if data is None:

        return render_template("NotUploaded.html")
    else:
        print(data[9])
        filename = data[9]

        return send_file('static/upload/' + filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
