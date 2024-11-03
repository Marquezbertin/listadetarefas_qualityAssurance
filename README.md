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
git clone https://github.com/seu-usuario/nome-do-repositorio.git

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

## Licença
Este projeto está licenciado sob a MIT License.