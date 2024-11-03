# Lista de Tarefas - Quality Assurance
Este projeto é uma aplicação web destinada a auxiliar QA testers a treinar e aprender a encontrar erros através de uma lista de tarefas. A aplicação permite a criação e gerenciamento de casos de teste, oferecendo uma maneira prática e eficiente de se familiarizar com as funcionalidades do software.

## Tabela de Conteúdos
* Características
* Tecnologias Utilizadas
* Instalação
* Uso
* Contribuição
* Casos de Testes Automatizados
* Licença

## Características
* Adicionar novos casos de teste.
* Editar casos de teste existentes.
* Excluir casos de teste.
* Filtrar casos de teste por status: Todas, Concluídas e Pendentes.
* Interface simples e intuitiva.

## Tecnologias Utilizadas
* HTML
* CSS
* JavaScript

## Instalação
Clone o repositório:

bash
git clone https://github.com/Marquezbertin/listadetarefas_qualityAssurance

Navegue até o diretório do projeto:
bash
Copiar código
cd nome-do-repositorio
Abra o arquivo index.html em seu navegador.

## Uso
Abra a aplicação no seu navegador.
Leia a introdução para entender o propósito da aplicação.
Siga as instruções passo a passo para criar e gerenciar seus casos de teste.
Utilize os botões de filtro para organizar seus casos de teste conforme necessário.

## Contribuição
Contribuições são bem-vindas! Se você deseja contribuir, siga estas etapas:
* Fork este repositório.
* Crie uma nova branch para sua feature (git checkout -b minha-feature).
* Faça suas alterações e commit (git commit -m 'Adiciona nova feature').
* Envie sua branch (git push origin minha-feature).
* Abra um Pull Request.

## Casos de Testes Automatizados 
Para garantir a funcionalidade da aplicação, um arquivo Python foi criado utilizando a biblioteca Selenium para realizar testes automatizados. Este arquivo testa as principais funcionalidades da aplicação, incluindo:

- Adição de novos casos de teste.
- Edição de casos de teste existentes.
- Exclusão de casos de teste.

#### Pré-requisitos

Antes de executar os testes, certifique-se de ter:

- Python instalado no seu sistema. [Download do Python](https://www.python.org/downloads/).
- Selenium instalado. Você pode instalar o Selenium usando o seguinte comando:

  ```bash
  pip install selenium
O ChromeDriver ou outro driver de navegador compatível baixado e adicionado ao seu PATH.
Executando os Testes
Crie um arquivo Python chamado test_app.py e insira o código de teste fornecido.

Atualize a linha que inicia a aplicação no script para o caminho do seu arquivo index.html.

Execute o script no terminal ou prompt de comando:

bash
Copiar código
python test_app.py
Os testes automatizados ajudarão a verificar se as funcionalidades da aplicação estão funcionando conforme o esperado, proporcionando um ambiente de aprendizado eficaz para QA testers.

## Testes Manuais 
Os testes manuais são uma abordagem essencial na garantia de qualidade de software, onde testadores validam funcionalidades e desempenho do sistema através de ações manuais. Eles incluem testes positivos, que verificam se o software atende às expectativas, e testes negativos, que buscam identificar falhas ao introduzir entradas inválidas ou inesperadas.

### Testes Positivos
* Validação de Entradas: Verifique se o campo de entrada aceita entradas de texto válidas sem quaisquer restrições.
Placeholder: Confirme que o texto do espaço reservado "Digite uma nova tarefa..." é exibido corretamente quando o campo de entrada está vazio.
* Variedade de Caracteres: Verifique se o campo de entrada permite que o usuário insira uma variedade de caracteres, incluindo letras, números e caracteres especiais.
* Limite de Caracteres: Certifique-se de que o campo de entrada lida corretamente com entradas de texto longas, respeitando um limite razoável (por exemplo, 255 caracteres).
* Limpeza de Campo: Valide se o campo de entrada é limpo corretamente após o envio de uma nova tarefa.

### Testes Negativos
* Campo Vazio: Tente enviar o campo de entrada sem inserir nenhum texto e verifique se uma mensagem de erro ou indicação é exibida.
* Espaços em Branco: Teste se o campo de entrada aceita apenas espaços em branco e verifique o feedback de validação.
* Entradas Longas: Verifique se o campo rejeita entradas de texto que excedem o limite esperado e exibe um erro apropriado.
* Caracteres Inválidos: Confirme que a inserção de caracteres inválidos (por exemplo, emojis ou caracteres de controle) não travam o aplicativo e são tratadas de maneira adequada.
* Teclas Especiais: Teste o comportamento do campo de entrada ao pressionar "Enter" sem texto.

### Cenários de Testes Criativos
* Copia e Cola: Simule um usuário tentando copiar e colar uma longa lista de tarefas no campo de entrada para observar como o aplicativo lida com entradas em massa.
* Digitação Rápida: Teste o comportamento do campo de entrada ao alternar rapidamente entre digitar e excluir texto, verificando a existência de problemas de desempenho.
* Atalhos de Teclado: Explore o efeito do uso de atalhos de teclado (como Ctrl+C, Ctrl+V) para garantir que o aplicativo mantém sua funcionalidade e integridade.
* Interação com Modais: Investigue como o campo de entrada responde quando um usuário tenta inserir texto enquanto um modal ou sobreposição está ativo na página.
* Condições do Navegador: Avalie o comportamento do campo de entrada sob diferentes condições do navegador (por exemplo, redimensionando a janela, usando diferentes níveis de zoom) para garantir uma experiência consistente do usuário.

## Licença
Este projeto está licenciado sob a MIT License.