from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request 
from flask import redirect , url_for
from flask_security  import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required 



app = Flask(__name__)

## DB 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@10.221.125.108/flaskmovie'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_PASSWORD_SALT'] = "double salting" 

db = SQLAlchemy(app)



# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))


#Setup Flask_security 
user_datastore = SQLAlchemyUserDatastore(db,User,Role)
security = Security(app,user_datastore)

#Create a user to test with 
#app.before_first_request
#def create_user():
#    db.create_all()
#    user_datastore.create_user(email='teste@gmail.com' , password = 'teste')
#    db.session.commit()

## Fim DB 


@app.route('/')
def index():
    # abaixo , comando para renderizar a pagina passando apos o nome do template , os objetos que serão exibidos
    return render_template('index.html')

@app.route('/post_user' , methods=['POST'])
def post_user():
    user=User(request.form['username'] , request.form['email'])
    db.session.add(user)
    db.session.commit()
    # o url_for pega o nome da funcao responsavel pela renderizacao da pagina de retorno 
    return redirect(url_for('index'))

#O nome que será enviado na url , precisa estar definido como parametro da funcção associada a rota 
@app.route('/profile/<email>')
@login_required        # o acesso a esta url agora está restrito a quem estiver logado 
def profile(email):
    user=User.query.filter_by(email=email).first() 
    return render_template('profile.html' , user = user)

if __name__ == "__main__":
    app.run()

