# DevSecOps Security Lab

Laboratório prático de DevSecOps desenvolvido para estudar vulnerabilidades de aplicações web, técnicas de exploração, remediação e automação de segurança em pipelines CI/CD.

## Objetivo

Este projeto foi criado para simular o ciclo de vida de vulnerabilidades em um ambiente controlado, permitindo:

* Desenvolver funcionalidades vulneráveis intencionalmente.
* Explorar vulnerabilidades de forma prática.
* Entender os impactos de negócio e segurança.
* Implementar correções seguindo boas práticas.
* Integrar ferramentas de segurança em pipelines DevSecOps.
* Automatizar a detecção de vulnerabilidades durante o desenvolvimento.

O foco principal é demonstrar a aplicação prática dos conceitos de Secure SDLC (Secure Software Development Lifecycle) e DevSecOps.

---

## Tecnologias Utilizadas

### Aplicação

* Python
* Flask
* SQLite
* HTML
* CSS

### Segurança

* GitHub Actions
* GitHub Advanced Security
* CodeQL (em implementação)

### Controle de Versão

* Git
* GitHub

---

## Metodologia

Cada vulnerabilidade segue o mesmo fluxo de trabalho:

```text
Implementação Vulnerável
        │
        ▼
Exploração Manual
        │
        ▼
Documentação
        │
        ▼
Detecção Automatizada
        │
        ▼
Correção
        │
        ▼
Validação
```

O objetivo não é apenas encontrar falhas, mas compreender todo o processo de identificação, correção e prevenção.

---

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

## Pipeline DevSecOps

Atualmente o projeto possui um pipeline de Integração Contínua em desenvolvimento utilizando GitHub Actions.

### Objetivos do Pipeline

* Automatizar validações de código.
* Preparar ambiente de execução.
* Instalar dependências.
* Executar testes automatizados.
* Integrar ferramentas de segurança.

### Fluxo Atual

```text
Push
 │
 ▼
GitHub Actions
 │
 ▼
Checkout do código
 │
 ▼
Configuração do Python
 │
 ▼
Instalação das dependências
```

### Próximas Implementações

* CodeQL
* Dependency Review
* Dependabot
* Secret Scanning
* Pull Request Security Gates
* Branch Protection Rules

---

## Estrutura do Projeto

```text
devsecops-security-lab/
│
├── app/
│
├── docs/
│   ├── sqli-error-based.md
│   └── sqli-auth-bypass.md
│
├── templates/
│
├── static/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
│
└── README.md
```

---

## Roadmap

### Fase 1 - SQL Injection

* [x] Implementação vulnerável
* [x] Exploração manual
* [x] Documentação
* [ ] Detecção com CodeQL
* [ ] Correção
* [ ] Revalidação

### Fase 2 - Cross Site Scripting (XSS)

* [ ] Implementação vulnerável
* [ ] Exploração
* [ ] Detecção automatizada
* [ ] Correção

### Fase 3 - Path Traversal

* [ ] Implementação vulnerável
* [ ] Exploração
* [ ] Detecção automatizada
* [ ] Correção

### Fase 4 - Command Injection

* [ ] Implementação vulnerável
* [ ] Exploração
* [ ] Detecção automatizada
* [ ] Correção

### Fase 5 - SSRF

* [ ] Implementação vulnerável
* [ ] Exploração
* [ ] Detecção automatizada
* [ ] Correção

### Fase 6 - Hardcoded Secrets

* [ ] Implementação vulnerável
* [ ] Detecção com Secret Scanning
* [ ] Remediação

---

## Objetivos de Aprendizado

Este laboratório está sendo utilizado para aprofundar conhecimentos em:

* Desenvolvimento Seguro
* DevSecOps
* CI/CD
* GitHub Actions
* GitHub Advanced Security
* SAST
* Segurança de Aplicações Web
* OWASP Top 10
* Automação de Segurança

---

## Aviso

Este projeto contém vulnerabilidades intencionais e foi desenvolvido exclusivamente para fins educacionais e laboratoriais.

Não utilize os exemplos apresentados em ambientes de produção.
