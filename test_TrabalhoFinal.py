from playwright.sync_api import sync_playwright
from pageObjects.pages.homePageCM import CollegeManager

with sync_playwright() as trabalhoFinal:
    browser = trabalhoFinal.chromium.launch(headless=False)
    page = browser.new_page()
    college_manager = CollegeManager(page)
    college_manager.visitar()
    college_manager.adicionarEstudante('Gustavo')
    college_manager.adicionarCurso('Sistemas de Informação')
    college_manager.adicionarCurso('Engenharia Mecânica')
    college_manager.adicionarCurso('Veterinária')
    college_manager.associarEstudanteCurso('1', '1')
    college_manager.adicionarDisciplina('1', 'Quality Assurance')
    college_manager.adicionarDisciplina('1', 'DevOps')
    college_manager.adicionarDisciplina('1', 'Fundamentos de Programação')
    college_manager.associarEstudanteDisciplina('1', '1')
    college_manager.associarEstudanteDisciplina('1', '2')
    college_manager.associarEstudanteDisciplina('1', '3')