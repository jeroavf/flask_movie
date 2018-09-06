from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request 
from flask import redirect , url_for


app = Flask(__name__)

## DB 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@10.221.125.108/flaskmovie'
app.debug = True
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(80) , unique = True  )
    email = db.Column(db.String(120), unique=True  )

    def __init__(self, username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r >' % self.username 


## Fim DB 


@app.route('/')
def index():
    myUser = User.query.all() 
    oneItem = User.query.filter_by(username="teste").first()
    # abaixo , comando para renderizar a pagina passando apos o nome do template , os objetos que serão exibidos
    return render_template('add_user.html', myUser=myUser , oneItem=oneItem)

@app.route('/post_user' , methods=['POST'])
def post_user():
    user=User(request.form['username'] , request.form['email'])
    db.session.add(user)
    db.session.commit()
    # o url_for pega o nome da funcao responsavel pela renderizacao da pagina de retorno 
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()

