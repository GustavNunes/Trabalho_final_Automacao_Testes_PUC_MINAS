# Trabalho final Automação de Testes PUC MINAS

Trabalho realizado utilizando o Framework PlayWright utilizando a linguagem Python.

<h2>Download do Projeto</h2>

```
  git clone https://github.com/GustavNunes/Trabalho_final_Automacao_Testes_PUC_MINAS.git
```

<h2>Instalação do Playwright com Python</h2>

```
  pip install pytest-playwright
```
<h2>Instalação dos navegadores do Playwright</h2>

```
  playwright install
```

<h2>Execução dos testes</h2>

```
  pytest
```

<h2>Execução dos testes com debug</h2>

<h4>Bash</h4>

```
  PWDEBUG=1 pytest -s
```
<h4>PowerShell</h4>

```
  $env:PWDEBUG=1
  pytest -s
```
<h4>Batch</h4>

```
  set PWDEBUG=1
  pytest -s
```

<h2>Script do Enunciado do Trabalho</h2>

- cria um aluno (student)
- cria 3 cursos (courses)
- inscreve o aluno no curso de id 1
- adiciona 3 matérias (disciplines) no curso de id 1
- inscreve o aluno nas matérias de id 1,2,3
