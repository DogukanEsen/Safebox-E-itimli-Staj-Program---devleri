from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#güvenlik için kullanıcı adı ve şifre kısımlarını sildim. 
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<kullaniciadi>:<parola>@localhost/todo_app'
db = SQLAlchemy(app)

"""    
    Bu sql query komutu ile todo_verileri isimli tablomuzu oluşturabiliriz. Primary key int olarak id, todo metinini tutan todo satırları vardır. 
    CREATE TABLE todo_verileri (
    id SERIAL PRIMARY KEY,
    todo VARCHAR(200) NOT NULL
);
"""
class Tododb(db.Model):
    __tablename__ = 'todo_verileri'
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(200))

    def __repr__(self):
        return f"<TodoItem(id={self.id}, todo='{self.todo}')>"

#Burası giriş sayfası, eğer todoyu ekle butonuna tıklanırsa post edilir. Post edilince htmlde content ismine sahip kısımdaki veriyi alıp veritabanına ekler.Eğer Get işleminde ise jinja template kullanarak veritabanındaki veriler yazılır.  
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        todo = request.form['content']
        todo_item = Tododb(todo=todo)
        db.session.add(todo_item)
        db.session.commit()
        return redirect('/')
    else:
        todo_items = Tododb.query.all()
        return render_template('index.html', todo_items=todo_items)

#Eğer todoyu ekle butonuna tıklanırsa burası çalışır. content ismine sahip veri alınır. tıklanan verinin idsine göre ismi bulunur ve yeni ismiyle değiştirilir. Güvenli bir uygulama için filtre kullandım.
@app.route('/update/<int:todo_id>', methods=['POST'])
def update(todo_id):
    yeni_todo = request.form['content']
    todo_item = Tododb.query.filter_by(id=todo_id).first()
    if todo_item:
        todo_item.todo = yeni_todo
        db.session.commit()
    return redirect('/')

#Burası sil tuşuna basınca çalışır. İlgili todo idsi ile veritabanında bulunur ve silinir. Güvenli bir uygulama için filtre kullandım.
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo_item = Tododb.query.filter_by(id=todo_id).first()
    if todo_item:
        db.session.delete(todo_item)
        db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    #Güvenlik için debug false
    app.run(debug=False)
