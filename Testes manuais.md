# Testes Manuais 

Testes Positivos:
   Verifique se o campo de entrada aceita entradas de texto válidos sem quaisquer restrições.  
   Teste se o texto do espaço reservado "Digite uma nova tarefa..." é exibido corretamente quando o campo de entrada está vazio.  
   Verifique se o campo de entrada permite que o usuário insira uma variedade de caracteres, incluindo letras, números e caracteres especiais.  
   -se de que o campo de entrada certifique-se de lidar com entradas de texto longas até um limite razoável (por exemplo, 255 caracteres).  
   Valide se o campo de entrada está limpo corretamente após enviar uma nova tarefa.  

Testes Negativos:
   Tente enviar o campo de entrada sem inserir nenhum texto e verifique se uma mensagem de erro ou indicação é exibida.  
   Teste se o campo de entrada aceita apenas espaços em branco (por exemplo, pressione a barra de espaço) e verifique o feedback de validação.  
   Verifique se o campo de entradas rejeita entradas de texto muito longas além do limite esperado e exibe um erro.  
   Verifique se a inserção de caracteres inválidos (por exemplo, emojis ou caracteres de controle) não trava o aplicativo e é tratada com elegância.  
   Teste o comportamento do campo de entrada quando ações especiais do teclado são realizadas, como pressionar "Enter" sem entrada.  

Cenários de Testes Criativos:
   Simule um usuário tentando copiar e colar uma longa lista de tarefas no campo de entrada para ver como o aplicativo lida com entradas em massa.  
   Teste o comportamento do campo de entrada quando o usuário alterna rapidamente entre digitar e excluir texto para verificar se há algum problema de atraso ou desempenho.  
   Explore o efeito do uso de atalhos de teclado (como Ctrl+C, Ctrl+V) para ver se o aplicativo mantém a funcionalidade e a integridade.  
   Investigue como o campo de entrada responde quando um usuário tenta inserir texto enquanto um modal ou sobreposição está ativo na página.  
   Avalie como o campo de entrada se comporta sob diferentes condições do navegador (por exemplo, redimensionando a janela, usando diferentes níveis de zoom) para garantir uma experiência consistente do usuário.  