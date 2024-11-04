Descrição dos Testes da Aplicação de Lista de Tarefas
Script 1: Teste de Adição e Remoção de Tarefa
Este script utiliza Selenium WebDriver para automatizar a interação com a aplicação de lista de tarefas, focando na adição e remoção de tarefas.

Estrutura do Script
Configuração do Driver: Inicializa o driver do Chrome.
Função Principal test_add_and_remove_task: Contém os passos para adicionar uma tarefa e, em seguida, removê-la.
Passos do Teste
Acessa a Página: Abre a URL da aplicação e aguarda o carregamento.

Adicionar uma Nova Tarefa:

Localiza o campo de entrada e insere "Nova Tarefa de Teste".
Localiza o botão "Adicionar" e clica nele.
Aguarda um pouco para garantir que a tarefa seja adicionada ao DOM.
Imprime a lista de tarefas atuais após a adição.
Verifica se a Tarefa foi Adicionada:

Utiliza WebDriverWait para encontrar a nova tarefa na lista.
Se a tarefa for encontrada, imprime confirmação e tenta excluir a tarefa.
Excluir a Tarefa:

Localiza o botão "Excluir" da tarefa recém-adicionada e clica nele.
Aguarda para garantir que a exclusão aconteça.
Verifica a Remoção:

Imprime a lista de tarefas atuais após a exclusão.
Verifica se a tarefa "Nova Tarefa de Teste" foi removida, imprimindo o resultado da verificação.
Tratamento de Erros: Inclui um bloco try-except para capturar e imprimir erros que possam ocorrer durante a execução do teste.

Script 2: Teste Automatizado com Unittest
Este script utiliza o módulo unittest em Python para estruturar testes automatizados com Selenium WebDriver, abordando várias funcionalidades da aplicação de lista de tarefas.

Estrutura do Script
Classe TodoAppTest: Contém métodos para cada caso de teste.
Configuração Inicial e Final:
setUpClass: Configura o WebDriver e abre a URL da aplicação.
tearDownClass: Encerra o WebDriver após a execução dos testes.
Casos de Teste

1. test_add_empty_task
Objetivo: Verificar se o sistema exibe um alerta ao tentar adicionar uma tarefa vazia.
Execução: Clica no botão "Adicionar" sem inserir texto, e valida a mensagem do alerta.
2. test_delete_specific_task
Objetivo: Testar a exclusão de uma tarefa específica.
Execução:
Adiciona uma tarefa "Teste de Exclusão".
Clica no botão "Excluir" e verifica se a tarefa foi removida da lista.
3. test_edit_task
Objetivo: Testar a edição de uma tarefa existente.
Execução:
Adiciona a tarefa "Tarefa para Edição".
Edita o texto da tarefa para "Tarefa Editada" usando JavaScript.
Verifica se a edição foi aplicada corretamente.
4. test_filter_completed_tasks
Objetivo: Testar a funcionalidade de filtragem de tarefas concluídas.
Execução:
Adiciona a tarefa "Tarefa Concluída" e a marca como completa.
Aplica o filtro de tarefas concluídas e verifica se a tarefa aparece na lista filtrada.
5. test_persistence_on_reload
Objetivo: Garantir que as tarefas persistem após recarregar a página.
Execução:
Adiciona "Tarefa Persistente".
Recarrega a página e verifica se a tarefa ainda está visível.
Execução do Script
A função unittest.main() executa todos os testes, permitindo a validação automatizada das funcionalidades da aplicação.
