# DevSecOps-Lab

## Vulnerabilidades Estudadas

### SQL Injection

Status: Concluído

#### Cenário

Foi implementada uma funcionalidade de autenticação vulnerável utilizando concatenação de strings para construção de consultas SQL.

#### Testes realizados

##### Error Based SQL Injection

Objetivo:

* Identificar falhas no tratamento de entrada.
* Observar mensagens de erro geradas pelo banco.

Documentação:

```text
docs/sqli-error-based.md
```

##### Authentication Bypass

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

#### Aprendizados

* Construção insegura de consultas SQL.
* Impacto da entrada controlada pelo usuário.
* Bypass de autenticação.
* Consultas parametrizadas.
* Mitigação de SQL Injection.

---
