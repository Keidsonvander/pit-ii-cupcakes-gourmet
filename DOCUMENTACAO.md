# Documentação do Projeto

## Identificação
Aluno: Lucas Seara Santos  
RGM: 34112324

## Projeto
Aplicação responsiva para venda online de cupcakes gourmet, desenvolvida como continuidade da PIT I.

## Objetivo
Transformar os requisitos levantados na PIT I em uma solução funcional, permitindo visualizar produtos, adicionar cupcakes ao carrinho, cadastrar os dados do cliente e registrar um pedido.

## Requisitos funcionais
- Exibir catálogo de cupcakes.
- Mostrar nome, descrição e preço dos produtos.
- Permitir adicionar produtos ao carrinho.
- Calcular o valor total do pedido.
- Solicitar nome, telefone e endereço do cliente.
- Validar campos obrigatórios.
- Registrar o pedido no banco de dados.
- Exibir confirmação após a finalização.

## Requisitos não funcionais
- Interface simples e responsiva.
- Navegação clara.
- Mensagens de validação compreensíveis.
- Organização em camadas, separando interface, lógica e persistência.
- Código armazenado e versionado em repositório Git.

## Tecnologias
- Front-end: HTML5, CSS3 e JavaScript.
- Back-end: Python com Flask.
- Banco de dados: SQLite para a versão acadêmica funcional.
- Arquitetura: separação inspirada no padrão MVC.

## Estrutura de dados
Tabela `pedidos`:
- id: identificador do pedido.
- cliente: nome do cliente.
- telefone: telefone de contato.
- endereco: endereço de entrega.
- itens: resumo dos itens selecionados.
- total: valor total do pedido.
- criado_em: data e hora do registro.

## Fluxo principal
1. Usuário acessa o catálogo.
2. Seleciona um ou mais cupcakes.
3. Os itens são adicionados ao carrinho.
4. O sistema apresenta o total.
5. Usuário informa seus dados.
6. O sistema valida os campos.
7. O pedido é enviado ao back-end.
8. O back-end valida os produtos e recalcula o total.
9. O pedido é armazenado no banco.
10. O sistema apresenta a confirmação ao usuário.

## Melhorias realizadas em relação à PIT I
A PIT I concentrou-se no levantamento de requisitos, histórias de usuários, backlog e critérios de aceitação. Nesta etapa, esses elementos foram convertidos em uma aplicação funcional, incluindo interface responsiva, carrinho, validações, persistência de pedidos e tratamento de mensagens ao usuário.
