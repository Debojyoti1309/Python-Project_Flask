from flask import Flask,render_template,request,redirect,session,flash,url_for
from functools import wraps
from flask_mysqldb import MySQL, MySQLdb
from flask_restful import Resource, Api

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskdb3'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)
 
#Login
@app.route('/') 
@app.route('/login',methods=['POST','GET'])
def login():
    status=True
    if request.method=='POST':
        email=request.form["email"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        cur.execute("select * from users where EMAIL=%s and UPASS=%s",(email,pwd))
        data=cur.fetchone()
        if data:
            session['logged_in']=True
            session['username']=data["UNAME"]
            flash('Login Successfully','success')
            return redirect('index')
        else:
            flash('Invalid Login. Try Again','danger')
    return render_template("login.html")
  
#check if user logged in
def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Unauthorized, Please Login','danger')
			return redirect(url_for('login'))
	return wrap
  
#Registration  
@app.route('/reg',methods=['POST','GET'])
def reg():
    status=False
    if request.method=='POST':
        name=request.form["uname"]
        email=request.form["email"]
        pwd=request.form["upass"]
        cur=mysql.connection.cursor()
        cur.execute("insert into users(UNAME,UPASS,EMAIL) values(%s,%s,%s)",(name,pwd,email))
        mysql.connection.commit()
        cur.close()
        flash('Registration Successfully. Login Here...','success')
        return redirect('login')
    return render_template("reg.html",status=status)

#Home page
@app.route("/home")
@is_logged_in
def home():
	return render_template('index.html')

# Index Product Page Redirection
@app.route("/index")
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
 
    cur.execute('SELECT * FROM products ORDER BY id')
    data = cur.fetchall()
  
    cur.close()
    return render_template('index.html', products = data)
    
#logout
@app.route("/logout")
def logout():
	session.clear()
	flash('You are now logged out','success')
	return redirect(url_for('login'))

# Add New products Section
@app.route('/add_product', methods=['POST'])
def add_product():
    conn = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        created_at = request.form['created_at']
        updated_at = request.form['updated_at']
        add_by_user = request.form[' add_by_user']
        cur.execute("INSERT INTO products (name, price, description, created_at, updated_at, add_by_user) VALUES (%s,%s,%s,%s,%s,%s)", (name, price, description, created_at, updated_at, add_by_user))
        mysql.connection.commit()   
        flash('Products Added successfully')
        return redirect(url_for('index'))

# Edit Existing products Section
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_products(id):
    conn = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  
    cur.execute('SELECT * FROM products WHERE id = {0}'.format(id))
    data = cur.fetchall()
    mysql.connection.commit() 
    cur.close() 
    print(data[0])
    return render_template('edit.html', products = data[0])

# Update Existing products Section
@app.route('/update/<id>', methods=['POST'])
def update_products(id):
    if request.method == 'POST':
        name = request.form['name']
        Price = request.form['Price']
        description = request.form['description']
        created_at = request.form['created_at']
        updated_at = request.form['updated_at']
        add_by_user = request.form['add_by_user']
        conn = mysql.connection.cursor()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("""
            UPDATE products
            SET name = %s,
                Price = %s,
                description = %s,
                created_at = %s,
                updated_at = %s,
                add_by_user = %s
            WHERE id = %s
        """, (name, Price, description, created_at, updated_at, add_by_user, id))
        flash('Products Updated Successfully')
        mysql.connection.commit()   
        return redirect(url_for('index'))

# Delete Existing products Section
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_Products(id):
    conn = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  
    cur.execute('DELETE FROM products WHERE id = {0}'.format(id))
    mysql.connection.commit()   
    flash('Products Removed Successfully')
    return redirect(url_for('index'))

    
if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)