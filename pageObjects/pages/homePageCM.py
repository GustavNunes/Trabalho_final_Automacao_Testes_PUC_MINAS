class CollegeManager:
    def __init__(self, page):
        self.page = page
        self.campo_estudante_nome = page.locator('input#student-nome')
        self.campo_estudante_curso_id = page.locator('input#student-id')
        self.campo_estudante_disciplina_id = page.locator('input#subscribe-student-id')
        self.campo_curso_nome = page.locator('input#course-nome')
        self.campo_curso_estudante_id = page.locator('input#course-id')
        self.campo_curso_disciplina_id = page.locator('input#course-discipline-id')
        self.campo_disciplina_nome = page.locator('input#discipline-nome')
        self.campo_disciplina_estudante_id = page.locator('input#subscribe-discipline-id')
        self.botao_adicionar_estudante = page.locator('button#student-btn')
        self.botao_adicionar_curso = page.get_by_role("button", name="Add course")
        self.botao_associar_estudante_curso = page.get_by_role("button", name="Subscribe student in course")
        self.botao_adicionar_disciplina = page.get_by_role("button", name="Add discipline")
        self.botao_associar_estudante_disciplina = page.get_by_role("button", name="Subscribe discipline")

    def visitar(self):
        self.page.goto("https://tdd-detroid.onrender.com")

    def adicionarEstudante(self, nome):
        self.campo_estudante_nome.fill(nome)
        self.botao_adicionar_estudante.click()
    
    def adicionarCurso(self, nome):
        self.campo_curso_nome.fill(nome)
        self.botao_adicionar_curso.click()
    
    def associarEstudanteCurso(self, estudanteId, cursoId):
        self.campo_estudante_curso_id.fill(estudanteId)
        self.campo_curso_estudante_id.fill(cursoId)
        self.botao_associar_estudante_curso.click()
        
    def adicionarDisciplina(self, cursoId, nome):
        self.campo_disciplina_nome.fill(nome)
        self.campo_curso_disciplina_id.fill(cursoId)
        self.botao_adicionar_disciplina.click()
        
    def associarEstudanteDisciplina(self, estudanteId, disciplinaId):
        self.campo_estudante_disciplina_id.fill(estudanteId)
        self.campo_disciplina_estudante_id.fill(disciplinaId)
        self.botao_associar_estudante_disciplina.click()