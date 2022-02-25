# Processo Seletivo I.Systems - Software Engineer - Ênfase em Python

Este repositório tem a finalidade de implementar o desâfio do processo seletivo Software Engineer na I.Systems com Ênfase em python. A implementação segue a especificação base contida [neste arquivo](Especificacao.pdf), com pequenas alterações.

## Variáveis de ambiente

Lembre-se que as variáveis de ambiente devem ser colocadas no arquivo `.env`, para facilitar, existe um arquivo `env.example` que pode ser usuado como referência, nele se encontra todas as variáveis de ambientes que podem ser modificadas. Na tabela abaixo existe as variáveis de ambiente junto com sua respectiva explicação, além dos valores que podem assumir.

Variável | Descrição | Exemplo | Default
-------- | --------- | ------- | -------
`FLASK_ENV` | Modo de execução | development | development
`DATABASE_URL` | URL para o banco de dados |  | 

## Para execução localmente

Para executar a aplicação você vai precisar executar uma instância do Postgres, podendo fazer isso através do docker-compose com o seguinte comando:

```bash
docker-compose up -d postgres-isystems
```

Lembrando de fazer as alterações no .env para compatibilizar com o banco de dados criado, e em seguida executar o comando abaixo para iniciar a aplicação:

```bash
pyhton run.py
```

## Para execução com dokcer-compose

Para executar a aplicação através do docker, se faz necessário executar o seguinte comando: 


```bash
docker-compose up -d
```

Com esse comando, será inicializado o NGINX como Load Balancer, Postgres e a Rest API, na configuração atual a aplicação é duplicada para testar a escalabilidade horizontal.

 ## Built With
 
 * [VSCode](https://code.visualstudio.com/) - Usado para edição dos arquivos.
  * [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Framework em python para criação de REST API.
 
 ## Authors
 
 * **Leoberto Soares** - [leossoaress](https://github.com/leossoaress)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details