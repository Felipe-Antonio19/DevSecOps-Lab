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

```sql
' OR 1=1 --
```

Documentação:

```text
docs/sqli-auth-bypass.md
```

## DETECÇÃO 
* Após a implementação do pipeline codeql.yml é possivel concretizar a presença da vulnerabilidade em dois locais:
  
*   Query de insert no banco de dados.
<img width="1284" height="811" alt="image" src="https://github.com/user-attachments/assets/90b96216-d90a-474a-93e8-f54c49f3cf59" />

*   Query de select no banco de dados.
<img width="957" height="303" alt="image" src="https://github.com/user-attachments/assets/230fbbc6-a239-45f2-8d8c-9628993ca9f0" />




#### Aprendizados

* Construção insegura de consultas SQL.
* Impacto da entrada controlada pelo usuário.
* Bypass de autenticação.
* Consultas parametrizadas.
* Mitigação de SQL Injection.

---
