# Trees I Planted

O objetivo da aplicação é permitir que o usuário registre todas as árvores que plantou ao longo de sua vida. A aplicação persistirá em um banco de dados sqlite3 todas as árvores criadas. Por meio da interface gráfica implementada no [frontend](https://github.com/alissons-repos/treesiplanted-frontend/) o usuário será capaz de visualizar, criar, editar e deletar facilmente suas árvores cadastradas.

Esse repositório github destina-se a armazenar apenas o backend da aplicação. Sua segunda parte está armazenada no repositório do [frontend](https://github.com/alissons-repos/treesiplanted-frontend/).

---
## Como executar 

Após clonar este repositório, vá pelo terminal até o diretório raiz `treesiplanted-backend`, e execute a sequência de comandos abaixo.

Observação: os comandos a seguir forma descritos para usuários do sistema operacional Windows.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Para instalar as dependências listadas em `requirements.txt`, execute:

```
(env)$ pip install -r requirements.txt
```

Este comando instalará todas as dependências python, descritas no arquivo `requirements.txt`.

Após a execução do código anterior, execute o comando abaixo para inicializar a API:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Caso queira, utilize o parâmetro reload para executar a aplicação em modo de desenvolvimento, que reiniciará o servidor automaticamente após qualquer mudança salva no código fonte.

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Em seu terminal aparecerá algo como:
```
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.2:5000
Press CTRL+C to quit
```

Abra a [http://localhost:5000/trees](http://localhost:5000/trees) em seu navegador para verificar a sua lista de árvores.
