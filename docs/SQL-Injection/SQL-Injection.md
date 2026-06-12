# SQL Injection 

## Concatenação de Strings em Consulta INSERT
### Vulnerabilidade

* **Categoria:** Improper Neutralization of Special Elements used in an SQL Command (CWE-89)
* **Local afetado:** Cadastro de usuários (`INSERT`)
* **Causa:** Concatenação de strings na construção da consulta SQL

---
### Código Vulnerável
```python
query = f"INSERT INTO users (name, email, senha) VALUES ('{name}', '{email}', '{password}')"
cursor.execute(query)
```

Neste exemplo, os dados recebidos do usuário são inseridos diretamente na consulta SQL sem qualquer mecanismo de parametrização.

---

### Como Reproduzir

1. Inicie a aplicação.
2. Acesse a tela de cadastro de usuários.
3. No campo **Name**, informe apenas:

```text
'
```

5. Envie o formulário.

### Evidência

```markdown
![SQL Injection Evidence]("C:\Users\felip\Documents\DevSecOps-lab\docs\SQL-Injection\Evidence1.png")
```

---

### Resultado Observado

A consulta SQL é corrompida e o SQLite lança um OperationalError, retornando erro 500 na aplicação.

---

### Impacto

A entrada do usuário influencia diretamente a sintaxe SQL, evidenciando ausência de parametrização e possibilitando exploração dependendo do contexto da consulta.

### Referências

* OWASP SQL Injection Prevention Cheat Sheet
* CWE-89: Improper Neutralization of Special Elements used in an SQL Command
* SQLite Documentation – Parameter Binding
