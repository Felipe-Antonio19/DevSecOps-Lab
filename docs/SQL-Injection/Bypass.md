# SQL Injection - Bypass de Autenticação

## Objetivo

Demonstrar como uma vulnerabilidade de SQL Injection em uma funcionalidade de login pode permitir que um usuário seja autenticado sem possuir credenciais válidas.

> **Aviso:** Este teste foi realizado exclusivamente em um laboratório controlado desenvolvido para fins educacionais.

---

## Cenário

A aplicação realiza a autenticação utilizando uma consulta SQL construída por concatenação de strings.

Exemplo simplificado:

```python
query = f"""
SELECT * FROM users
WHERE email = '{email}'
AND password = '{password}'
"""
```

Como os valores fornecidos pelo usuário são inseridos diretamente na consulta, um atacante pode modificar sua lógica.

---

## Payload utilizado
### Email
```
aa@gmail.com
```
### Senha
```
' OR 1=1 --
```

---

## Consulta gerada

Após a interpolação dos dados, a consulta torna-se:

```sql
SELECT * FROM users
WHERE email = 'aa@gmail.com'
AND password = '' OR 1=1 --'
```

O operador `OR 1=1` cria uma condição que sempre será verdadeira.

Além disso, o comentário `--` faz com que o restante da consulta seja ignorado pelo interpretador SQL.

---

## Resultado observado

Mesmo informando um endereço de e-mail inexistente e uma senha inválida, a aplicação autentica o usuário.

Isso ocorre porque a consulta retorna pelo menos um registro da tabela `users`.

Em muitos casos, a função `fetchone()` retorna o primeiro usuário encontrado, e a aplicação interpreta esse resultado como uma autenticação válida.

Exemplo simplificado:

```python
user = cursor.fetchone()

if user:
    session["user"] = user["id"]
```

Como `user` não é nulo, o login é concedido.

---

## Fluxo do ataque

```text
Usuário envia:
Email    -> aa@gmail.com
Senha    -> ' OR 1=1 --

        │
        ▼

Aplicação monta a consulta SQL vulnerável

        │
        ▼

SELECT * FROM users
WHERE email='aa@gmail.com'
AND password='' OR 1=1

        │
        ▼

A condição OR 1=1 torna o WHERE verdadeiro

        │
        ▼

O banco retorna um usuário existente

        │
        ▼

A aplicação verifica apenas se existe um resultado

        │
        ▼

Login concedido indevidamente
```

---

## Impacto

Uma vulnerabilidade desse tipo pode permitir:

* Bypass completo da autenticação.
* Acesso não autorizado à aplicação.
* Login como outro usuário existente.
* Comprometimento de contas privilegiadas, como administradores.
* Exposição de informações sensíveis armazenadas no sistema.

Caso o primeiro registro da tabela pertença a um administrador, o atacante pode obter privilégios elevados sem conhecer nenhuma credencial válida.

---

## Causa raiz

O problema não está no payload em si, mas na forma como a consulta SQL é construída.
Ao concatenar diretamente dados controlados pelo usuário, o banco interpreta parte da entrada como comandos SQL em vez de tratá-la apenas como texto.

---
