from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver
driver = webdriver.Chrome()  # ou webdriver.Firefox() se estiver usando Firefox

# Acesse a aplicação
driver.get("file:///caminho/para/seu/index.html")  # Substitua pelo caminho do seu arquivo HTML

# Testa a adição de uma nova tarefa
def test_add_task():
    new_task_input = driver.find_element(By.ID, "new-task")
    new_task_input.send_keys("Novo Caso de Teste")
    add_button = driver.find_element(By.XPATH, "//button[text()='Adicionar']")
    add_button.click()
    time.sleep(1)  # Aguarda um segundo para que a tarefa seja adicionada

    # Verifica se a nova tarefa foi adicionada à lista
    task_list = driver.find_element(By.ID, "task-list")
    assert "Novo Caso de Teste" in task_list.text

# Testa a edição de uma tarefa
def test_edit_task():
    task_item = driver.find_element(By.XPATH, "//li[contains(text(), 'Novo Caso de Teste')]")
    task_item.click()  # Ativa o modo de edição
    task_item.clear()
    task_item.send_keys("Caso de Teste Editado")
    task_item.send_keys(Keys.RETURN)  # Simula pressionar Enter
    time.sleep(1)

    # Verifica se a tarefa foi editada
    task_list = driver.find_element(By.ID, "task-list")
    assert "Caso de Teste Editado" in task_list.text

# Testa a exclusão de uma tarefa
def test_delete_task():
    delete_button = driver.find_element(By.XPATH, "//li[contains(text(), 'Caso de Teste Editado')]//following-sibling::button")
    delete_button.click()
    time.sleep(1)

    # Verifica se a tarefa foi excluída
    task_list = driver.find_element(By.ID, "task-list")
    assert "Caso de Teste Editado" not in task_list.text

# Executa os testes
test_add_task()
test_edit_task()
test_delete_task()

# Fecha o navegador
driver.quit()
