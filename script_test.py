from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do driver
driver = webdriver.Chrome()

def test_add_and_remove_task():
    driver.get("https://marquezbertin.github.io/listadetarefas_qualityAssurance/")
    time.sleep(3)  # Espera para garantir que a página carregue

    # Adicionar uma nova tarefa
    try:
        input_task = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/input"))
        )
        print("Campo de entrada encontrado!")

        input_task.send_keys("Nova Tarefa de Teste")
        
        # Verifica se o botão de adicionar está presente
        add_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Adicionar']"))
        )
        print("Botão 'Adicionar' encontrado!")
        
        add_button.click()

        # Espera um pouco para garantir que a tarefa foi adicionada ao DOM
        time.sleep(4)

        # Imprimir as tarefas atuais antes da verificação
        task_items_atualizados = driver.find_elements(By.XPATH, "//ul[@id='task-list']//li")
        print("Tarefas atuais na lista após adição:")
        for item in task_items_atualizados:
            print(item.text)

        # Verificação mais robusta da nova tarefa
        try:
            task_item = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//ul[@id='task-list']//li[span[contains(text(), 'Nova Tarefa de Teste')]]"))
            )
            print("A nova tarefa foi encontrada na lista.")

            if task_item:
                print("A tarefa foi adicionada com sucesso!")

                # Agora, vamos tentar excluir a tarefa correspondente
                excluir_botao = task_item.find_element(By.XPATH, ".//button[contains(text(), 'Excluir')]")
                excluir_botao.click()  # Clica no botão "Excluir" da tarefa recém adicionada
                time.sleep(2)  # Espera para garantir que a exclusão aconteça

                # Verifique novamente as tarefas atuais
                task_items_atualizados = driver.find_elements(By.XPATH, "//ul[@id='task-list']//li")
                print("Tarefas atuais na lista após exclusão:")
                for item in task_items_atualizados:
                    print(item.text)

                # Verifica se a nova tarefa foi removida
                if all("Nova Tarefa de Teste" not in item.text for item in task_items_atualizados):
                    print("A tarefa foi removida com sucesso!")
                else:
                    print("A tarefa ainda está na lista, falha na exclusão!")

        except Exception as e:
            print("Erro ao verificar a nova tarefa:", e)
            print("Verifique se a tarefa foi realmente adicionada ou se o XPath está correto.")

    except Exception as e:
        print(f"Erro: {e}")
        print("Stacktrace completo:", e.__traceback__)  # Imprime o stacktrace completo

if __name__ == "__main__":
    try:
        test_add_and_remove_task()
    finally:
        driver.quit()
