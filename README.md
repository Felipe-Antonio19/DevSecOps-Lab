# SQL-INJECTION

#### Cenário
Foi implementada uma funcionalidade de autenticação vulnerável utilizando concatenação de strings para construção de consultas SQL.

## Testes realizados

### Error Based SQL Injection

Objetivo:

* Identificar falhas no tratamento de entrada.
* Observar mensagens de erro geradas pelo banco.

Documentação:

```text
docs/sqli-error-based.md
```

### Authentication Bypass

Objetivo:

* Manipular a lógica da consulta SQL.
* Realizar autenticação sem credenciais válidas.

Payload utilizado:

Atualmente o projeto possui um pipeline de Integração Contínua e um para análise do CodeQl utilizando GitHub Actions.

```sql
' OR 1=1 --
```


Documentação:

* Automatizar validações de código.
* Preparar ambiente de execução.
* Instalar dependências.
* Executar testes automatizados. (Em desenvolvimento)
* Executar testes de segurança (CodeQl)

### Fluxo Atual

```text
docs/sqli-auth-bypass.md
```


## DETECÇÃO 
* Após a implementação do pipeline codeql.yml é possivel concretizar a presença da vulnerabilidade em dois locais:
  
*   Query de insert no banco de dados.
<img width="1284" height="811" alt="image" src="https://github.com/user-attachments/assets/90b96216-d90a-474a-93e8-f54c49f3cf59" />

*   Query de select no banco de dados.
<img width="957" height="303" alt="image" src="https://github.com/user-attachments/assets/230fbbc6-a239-45f2-8d8c-9628993ca9f0" />

## CORREÇÃO

#### Adicionando consultas parametrizadas respectivamente em ambas as queries

```python
res = cursor.execute("SELECT * FROM users WHERE email = '?' AND senha = '?'", (email, password)).fetchone()
```

```python
cursor.execute("INSERT INTO users (name, email, senha) VALUES (?,?,?)", (name, email, password))
```

#### Pode-se notar a ausência da detecção da vulnerabilidade no ambiente pelo CodeQl

<img width="1292" height="544" alt="image" src="https://github.com/user-attachments/assets/f7449f7b-61f2-445b-a5a5-d781b39f28c7" />

#### Aprendizados

* Construção insegura de consultas SQL.
* Impacto da entrada controlada pelo usuário.
* Bypass de autenticação.
* Consultas parametrizadas.
* Mitigação de SQL Injection.
---

#### Referencia OWASP - https://owasp.org/Top10/2021/pt-BR/A03_2021-Injection/
Este projeto contém vulnerabilidades intencionais e foi desenvolvido exclusivamente para fins educacionais e laboratoriais.

Não utilize os exemplos apresentados em ambientes de produção.
>>>>>>> a761e4a (Revise README for CI pipeline and CodeQL updates)
