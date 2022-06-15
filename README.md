# :book: School API

Simples API para cadastro de cursos e avaliação de cursos.



## :link:Referência

 - [Crie APIs REST com Python e Django REST Framework: Essencial](https://www.udemy.com/course/criando-apis-rest-com-django-rest-framework-essencial/)


## :hammer: Instalação

Instale school-api com docker

```bash
  git clone https://github.com/isaias0rt0n/school-api.git
  cd school-api
  docker-compose up
```
Rodando as migrations
```bash
  docker-compose exec app python manage.py makemigrations
  docker-compose exec app python manage.py migrate
```
    
## Rodando os testes

Para rodar os testes, rode o seguinte comando
- Lembrando de configurar no ```settings.py``` a autenticação para TokenAuthentication
```bash
  python test_pytest.py
```


## :gear:Deploy

Deploy do Projeto na AWS/Azure


```Coming soon!```


## :label:Documentação
[http://localhost:8000/docs](http://localhost:8000/docs)

### Obter Token de Acesso

#### Cadastrar um usuário

```http
  POST http://localhost:8000/api/users/
```

#### Exemplo
```bash
curl --request POST \
--url http://localhost:8000/api/users/ \
--header 'Content-Type: application/json' \
--data '{
"username": "user_1",
"password": "123456789"
}'
```

#### Resposta
```bash
{
  "username": "user_1"
}
```


#### Geração de Token
Campos: ```grant_type, client_id, client_secret, username, password, scope```

```bash
curl -X POST \
--data '{"grant_type": "password", "client_id": "", "client_secret": "", "username": "", "password": <>, "scope": "write"}' \
> --header 'Content-Type: application/json' \
> --url http://localhost:8000/o/token/
```

#### Resposta
```bash
{
	"access_token": "6gMqKXWD9n0JX9r7WQ4GI955CBw14A",
	"expires_in": 36000,
	"token_type": "Bearer",
	"scope": "write",
	"refresh_token": "QUoIDI2HqTh0Zge3OK0rbNR7SoohBC"
}
```




## Autores

- [@isaias0rt0n](https://www.github.com/isaias0rt0n)
