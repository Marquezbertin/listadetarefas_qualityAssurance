from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura o driver (aqui usando Chrome)
driver = webdriver.Chrome()  # Se o chromedriver estiver no PATH

try:
    # Abre a página
    driver.get("https://marquezbertin.github.io/listadetarefas_qualityAssurance/")
    time.sleep(2)  # espera carregar a página

    # Encontrar campo de texto para nova tarefa (analisar o site e adaptar o seletor)
    input_tarefa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "task-input"))
    )
    input_tarefa.send_keys("Teste com Selenium")
    input_tarefa.send_keys(Keys.RETURN)  # Pressiona Enter para adicionar

    time.sleep(2)  # espera a tarefa aparecer na lista

    # Marcar a tarefa como concluída (exemplo - adaptar o seletor)
    tarefa = driver.find_element(By.XPATH, "//li[contains(text(), 'Teste com Selenium')]")
    tarefa.click()  # se clicar marca como concluída (depende da implementação)

    time.sleep(2)

    # Deletar a tarefa (exemplo)
    botao_deletar = tarefa.find_element(By.CLASS_NAME, "delete-button")  # adaptar para seu botão
    botao_deletar.click()

    time.sleep(2)

finally:
    driver.quit()
