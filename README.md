### Aplicacao basica para enteder o funcionamento do flask associado a um template bootstrap  
* Estrutura inicial  


>> $ cd app_path   
>> $ mkdir -p static/css  
>> $ mkdir -p static/images  
>> $ mkdir -p static/js  
>> $ mkdir -p templates   
>> $ vi app.py  
>>    from flask import Flask     
>>    from flask_sqlalchemy import SQLAlchemy    
>>    app = Flask(__name__)    
>>  
>>    @app.route('/')    
>>    def index():    
>>        return "<h1 style='color: red'>hello Flask</h1>"    
>>  
>>    if __name__ == "__main__":    
>>        app.run()    

- Bibliotecas   
 pip install flask  
 pip install Flask-SQLAlchemy  
 pip install psycopg2  


- Banco de dados postgres rodando em container   
docker run --name postgres -e POSTGRES_PASSWORD='1234'  -p 5432:5432 -d postgres  

* atencao para erro no login no docker hub : o docker do mac estava logado com o email e nao com o docker id , que é só o id_docker 

* pgadmin para acessar administrar o  postgres:  
docker pull dpage/pgadmin4  
docker run -p 8000:80  -e "PGADMIN_DEFAULT_EMAIL=usuario@a.com"  -e "PGADMIN_DEFAULT_PASSWORD=1234" -d dpage/pgadmin4  

- usuario postgres : postgress/password  

- Criando a tabela do usuario   
$ python   

>>> from app import db   
>>> db.create_all()  