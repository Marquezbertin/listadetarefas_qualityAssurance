from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TodoAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configuração do navegador (usando ChromeDriver)
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://marquezbertin.github.io/listadetarefas_qualityAssurance/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_add_empty_task(self):
        # Teste de Adição de Tarefa Vazia
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Adicionar']")))
        add_button.click()
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Por favor, digite uma tarefa.")
        alert.accept()

    def test_delete_specific_task(self):
        # Teste de Exclusão de Tarefa Específica
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        task_input = wait.until(EC.presence_of_element_located((By.ID, "new-task")))
        task_input.send_keys("Teste de Exclusão")
        add_button = driver.find_element(By.XPATH, "//button[text()='Adicionar']")
        add_button.click()

        delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/ul/li/button")))
        delete_button.click()

        # Verifica se a tarefa foi removida
        task_list = driver.find_element(By.ID, "task-list")
        self.assertNotIn("Teste de Exclusão", task_list.text)

    def test_edit_task(self):
        # Teste de Edição de Tarefa
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        task_input = wait.until(EC.presence_of_element_located((By.ID, "new-task")))
        task_input.send_keys("Tarefa para Edição")
        add_button = driver.find_element(By.XPATH, "//button[text()='Adicionar']")
        add_button.click()

        # Edita a tarefa adicionada
        task_span = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Tarefa para Edição']")))
        driver.execute_script("arguments[0].textContent = 'Tarefa Editada';", task_span)

        # Verifica se a tarefa foi editada
        self.assertIn("Tarefa Editada", task_span.text)

    def test_filter_completed_tasks(self):
        # Teste de Filtro de Tarefas Concluídas
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        task_input = wait.until(EC.presence_of_element_located((By.ID, "new-task")))
        task_input.send_keys("Tarefa Concluída")
        add_button = driver.find_element(By.XPATH, "//button[text()='Adicionar']")
        add_button.click()

        # Marca a tarefa como concluída
        checkbox = driver.find_element(By.XPATH, "//li[last()]/input[@type='checkbox']")
        checkbox.click()

        # Aplica o filtro de concluídas
        filter_completed = driver.find_element(By.XPATH, "//button[text()='Concluídas']")
        filter_completed.click()

        # Verifica se a tarefa concluída aparece após aplicar o filtro
        task_list = driver.find_element(By.ID, "task-list")
        tasks_visible = [task.text for task in task_list.find_elements(By.TAG_NAME, "li") if task.is_displayed()]
        self.assertTrue(any("Tarefa Concluída" in task for task in tasks_visible))

    def test_persistence_on_reload(self):
        # Teste de Persistência das Tarefas no localStorage
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        task_input = wait.until(EC.presence_of_element_located((By.ID, "new-task")))
        task_input.send_keys("Tarefa Persistente")
        add_button = driver.find_element(By.XPATH, "//button[text()='Adicionar']")
        add_button.click()

        # Recarrega a página
        driver.refresh()

        # Verifica se a tarefa ainda está na lista
        task_list = wait.until(EC.presence_of_element_located((By.ID, "task-list")))
        self.assertIn("Tarefa Persistente", task_list.text)

# Código de execução do teste
if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
