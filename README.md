# Trabalho final Automação de Testes PUC MINAS

Trabalho realizado utilizando o Framework PlayWright utilizando a linguagem Python.

<H2>Download do Projeto</H2>

```http
  git clone https://github.com/GustavNunes/Trabalho_final_Automacao_Testes_PUC_MINAS.git
```

<H2>Instalação do Playwright com Python</H2>

```http
  pip install pytest-playwright
```
<H2>Instalação dos navegadores do Playwright</H2>

```http
  playwright install
```

<h2>Execução dos testes</h2>

```http
  pytest
```

<h2>Execução dos testes com debug</h2>

<h4>Bash</h4>

```http
  PWDEBUG=1 pytest -s
```
<h4>PowerShell</h4>

```http
  $env:PWDEBUG=1
  pytest -s
```
<h4>Batch</h4>

```http
  set PWDEBUG=1
  pytest -s
```

<h2>Script do Enunciado do Trabalho</h2>

- cria um aluno (student)
- cria 3 cursos (courses)
- inscreve o aluno no curso de id 1
- adiciona 3 matérias (disciplines) no curso de id 1
- inscreve o aluno nas matérias de id 1,2,3
