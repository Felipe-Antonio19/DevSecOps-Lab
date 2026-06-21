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

## Pipeline DevSecOps

Atualmente o projeto possui um pipeline de Integração Contínua e um para análise do CodeQl utilizando GitHub Actions.

### Objetivos do Pipeline

* Automatizar validações de código.
* Preparar ambiente de execução.
* Instalar dependências.
* Executar testes automatizados. (Em desenvolvimento)
* Executar testes de segurança (CodeQl)

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

---

## Roadmap

### Fase 1 - SQL Injection

* [x] Implementação vulnerável
* [x] Exploração manual
* [x] Documentação
* [x] Detecção com CodeQL
* [x] Correção
* [x] Validação

### Fase 2 - Broken Access Control

* [ ] Implementação vulnerável
* [ ] Exploração
* [ ] Documentação
* [ ] Detecção automatizada
* [ ] Correção
* [ ] Validação

---

## Objetivos de Aprendizado

Este laboratório está sendo utilizado para aprofundar conhecimentos em:

* Desenvolvimento Seguro
* DevSecOps
* CI/CD
* GitHub Actions
* Estudo para certificação GitHub Advanced Security
* SAST
* Segurança de Aplicações Web
* OWASP Top 10
* Automação de Segurança

---

## Aviso

Este projeto contém vulnerabilidades intencionais e foi desenvolvido exclusivamente para fins educacionais e laboratoriais.

Não utilize os exemplos apresentados em ambientes de produção.
