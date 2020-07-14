from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL


app= Flask(__name__)
app.secret_key="flash message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='intern'

mysql = MySQL(app)




@app.route('/')
def Index():

    cur = mysql.connection.cursor()
    cur.execute("SELECT employee.EMP_ID,employee.EMP_NAME,employee.EMP_ADDRESS,employee.DESIGNATION,employee.DOB,employee.TELEPHONE,employee.Email,department.DEPT_NAME FROM employee,department WHERE employee.DEPT_ID=department.DEPT_ID")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html',employee = data)


@app.route('/',methods=['POST','GET'])
def my_form():
    text = request.form['DEP']
    cur= mysql.connection.cursor()
    cur1=mysql.connection.cursor()
    cur1.execute("SELECT DEPT_ID FROM department WHERE DEPT_NAME=%s",(text,))
    RESULT = cur1.fetchall()
    cur.execute("SELECT employee.EMP_ID,employee.EMP_NAME,employee.EMP_ADDRESS,employee.DESIGNATION,employee.DOB,employee.TELEPHONE,employee.Email,department.DEPT_NAME FROM employee,department WHERE employee.DEPT_ID=department.DEPT_ID && employee.DEPT_ID=%s",(RESULT,))
    Data = cur.fetchall()
    return render_template('dep.html', employee=Data)






@app.route('/insert',methods=['POST'])
def insert():
    if request.method=="POST":
        flash("Data Inserted Successfully")

        NAME = request.form['NAME']
        ADDRESS =request.form['ADDRESS']
        DESIGNATION = request.form['DESIGNATION']
        DOB = request.form['DOB']
        TELEPHONE = request.form['TELEPHONE']
        EMAIL=request.form['EMAIL']
        DEPT_NAME=request.form['DEPT_NAME']
        cur = mysql.connection.cursor()
        cur1 = mysql.connection.cursor()
        cur.execute("SELECT DEPT_ID from department where DEPT_NAME= %s ",(DEPT_NAME,))
        RESULT = cur.fetchall()
        cur1.execute("INSERT INTO employee (EMP_NAME,EMP_ADDRESS,DESIGNATION,DOB,TELEPHONE,EMAIL,DEPT_ID) VALUES (%s,%s,%s,%s,%s,%s,%s) ",(NAME,ADDRESS,DESIGNATION,DOB,TELEPHONE,EMAIL,RESULT))
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/dinsert',methods=['POST'])
def dinsert():
    if request.method=="POST":
        flash("Data Inserted Successfully")
        DNAME=request.form['DNAME']
        DADDRESS=request.form['DADDRESS']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO department(DEPT_NAME,DEPT_ADDRESS)VALUES(%s,%s)",(DNAME,DADDRESS))
        mysql.connection.commit()
        return redirect(url_for('Index'))



@app.route('/update',methods = ['POST','GET'])
def update():
    if request.method == 'POST':
        EMP_ID=request.form['id']
        NAME = request.form['NAME']
        ADDRESS = request.form['ADDRESS']
        DESIGNATION = request.form['DESIGNATION']
        DOB = request.form['DOB']
        TELEPHONE = request.form['TELEPHONE']
        EMAIL = request.form['EMAIL']
        DEPT_NAME = request.form['DEPT_NAME']
        cur = mysql.connection.cursor()
        cur1= mysql.connection.cursor()
        cur1.execute("SELECT DEPT_ID from department where DEPT_NAME= %s ",(DEPT_NAME,))
        RESULT = cur1.fetchall()
        cur.execute("""UPDATE employee SET EMP_NAME=%s,EMP_ADDRESS=%s,DESIGNATION=%s,DOB=%s,TELEPHONE=%s,EMAIL=%s,DEPT_ID=%s WHERE EMP_ID=%s""",
                    (NAME,ADDRESS,DESIGNATION,DOB,TELEPHONE,EMAIL,RESULT,EMP_ID))
        flash("Data Updated SuccessFully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods=['POST','GET'])
def delete(id_data):

    flash("Employee Deleted Successfully")

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employee WHERE EMP_ID= %s ", (id_data))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/back')
def back():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
