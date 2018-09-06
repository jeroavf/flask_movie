- Banco de dados postgres rodando em container 
docker run --name postgres -e POSTGRES_PASSWORD='1234' -d postgres

* atencao para erro no login no docker hub : o docker do mac estava logado com o email e nao com o docker id , que é só o id_docker 

* pgadmin para acessar administrar o  postgres a
docker pull dpage/pgadmin4
docker run -p 8000:80 \
-e "PGADMIN_DEFAULT_EMAIL=usuario@a.com" \
-e "PGADMIN_DEFAULT_PASSWORD=password" \
-d dpage/pgadmin4

- usuario postgres : postgress/password