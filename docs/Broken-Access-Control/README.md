# Broken Access Control (A01:2021) - OWASP Top 10

## Visão geral da vulnerabilidade

Broken Access Control é uma das vulnerabilidades mais críticas listadas no OWASP Top 10 (A01:2021). Ela ocorre quando uma aplicação falha em aplicar corretamente restrições de autorização, permitindo que usuários acessem ou manipulem recursos fora de seus privilégios definidos.

Esse tipo de falha não está relacionado à autenticação (identidade do usuário), mas sim à autorização (o que o usuário pode fazer dentro do sistema após autenticar).

---

## Testes realizados

### Horizontal Privilege Escalation

Vulnerabilidade ocorrida quando não há parâmetro de owner_id na requisição de dados ao banco de dados, visto que, nesta aplicação cada usuário deveria ter acesso a leitura apenas das suas próprias tasks.

![Código Vulneravel](image-1.png)

![Horizontal Escalation](image.png)

No exemplo acima, o usuário logado como "Felipe" consegue visualizar a task criada por "Maria".

---

### Insecure Direct Object Reference (IDOR)

IDOR é uma técnica de ataque da vulnerabilidade Broken Access Control que ocorre o servidor não realiza uma checagem se o usuário possui autorização para realizar determinada ação. Com isso um usuário A consegue manipular um identificador de outro usuário. Neste exemplo, o usuário Felipe consegue enviar task_id de uma task da Maria e exclui-la.
![Task da Maria](image.png)

Com este ID o usuário A consegue enviar a requisição para exclusão da task de Maria

![Requisição de exclusão](image-1.png)

Com isso as task podem ser deletadas por qualquer usuário.

![Resultado](image-2.png)


