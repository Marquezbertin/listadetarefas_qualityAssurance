from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from datetime import datetime
import time

class NewTaskTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configura o driver do Chrome e inicializa o relatório
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://marquezbertin.github.io/listadetarefas_qualityAssurance/')
        cls.report = []  # Lista para armazenar os resultados dos testes

    @classmethod
    def tearDownClass(cls):
        # Fecha o navegador e salva o relatório em um arquivo TXT após todos os testes
        cls.driver.quit()
        with open("test_report.txt", "w", encoding="utf-8") as file:
            file.write("Relatório de Testes:\n")
            file.write("\n".join(cls.report))

    def log_test_result(self, test_name, description, expected, actual, result):
        # Registra os detalhes do teste no relatório
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__class__.report.append(
            f"Data e Hora: {timestamp}\n"
            f"Teste: {test_name}\n"
            f"Descrição: {description}\n"
            f"Resultado Esperado: {expected}\n"
            f"Resultado Encontrado: {actual}\n"
            f"Resultado: {result}\n"
            f"{'-'*50}"
        )

    def test_enter_new_task(self):
        # Testa se é possível inserir uma nova tarefa no campo de entrada
        test_name = "Inserir nova tarefa"
        description = "Verifica se o campo de entrada aceita texto e exibe o valor inserido."
        task = 'Buy groceries'
        input_field = self.driver.find_element(By.CSS_SELECTOR, '#new-task')
        input_field.send_keys(task)  # Insere o texto no campo
        input_value = input_field.get_attribute('value')  # Obtém o valor do campo
        expected = task
        actual = input_value
        result = "PASSOU" if expected == actual else "FALHOU"
        self.log_test_result(test_name, description, expected, actual, result)
        self.assertEqual(actual, expected)

    def test_clear_input_field(self):
        # Testa se o campo de entrada pode ser limpo
        test_name = "Limpar campo de entrada"
        description = "Verifica se o campo de entrada pode ser limpo após inserir texto."
        task = 'Buy groceries'
        input_field = self.driver.find_element(By.CSS_SELECTOR, '#new-task')
        input_field.send_keys(task)  # Insere o texto no campo
        input_field.clear()  # Limpa o campo
        input_value = input_field.get_attribute('value')  # Obtém o valor do campo
        expected = ''
        actual = input_value
        result = "PASSOU" if expected == actual else "FALHOU"
        self.log_test_result(test_name, description, expected, actual, result)
        self.assertEqual(actual, expected)

    def test_input_placeholder(self):
        # Testa se o campo de entrada possui o placeholder correto
        test_name = "Placeholder do campo de entrada"
        description = "Verifica se o campo de entrada exibe o placeholder correto."
        input_field = self.driver.find_element(By.CSS_SELECTOR, '#new-task')
        placeholder = input_field.get_attribute('placeholder')  # Obtém o atributo placeholder
        expected = 'Digite uma nova tarefa...'
        actual = placeholder
        result = "PASSOU" if expected == actual else "FALHOU"
        self.log_test_result(test_name, description, expected, actual, result)
        self.assertEqual(actual, expected)

    def test_input_max_length(self):
        # Testa se o campo de entrada possui um limite máximo de caracteres
        test_name = "Limite máximo de caracteres"
        description = "Verifica se o campo de entrada possui um limite máximo de 70 caracteres."
        input_field = self.driver.find_element(By.CSS_SELECTOR, '#new-task')
        max_length = input_field.get_attribute('maxlength')  # Obtém o atributo maxlength
        expected = '70'
        actual = max_length
        result = "PASSOU" if expected == actual else "FALHOU"
        self.log_test_result(test_name, description, expected, actual, result)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()