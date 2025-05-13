Este projeto implementa um sistema de Quiz interativo baseado em cliente-servidor, utilizando sockets TCP para comunicação. O objetivo é permitir que múltiplos clientes se conectem ao servidor, respondam a perguntas de um quiz e recebam sua pontuação ao final. O projeto foi desenvolvido como parte de uma atividade acadêmica, com foco em arquitetura modular, interoperabilidade e uso de protocolos de comunicação personalizados.

# Arquitetura do Projeto

A estrutura do projeto é organizada da seguinte forma:

# Componentes Principais

## Servidor (server/server.py)

O servidor é responsável por carregar as perguntas do quiz, gerenciar conexões de clientes e enviar/receber mensagens utilizando o protocolo definido. Ele suporta múltiplos clientes simultaneamente através de threads.

## Cliente (client/client.py)

O cliente conecta-se ao servidor, recebe as perguntas, envia as respostas e exibe a pontuação final ao usuário.

## Protocolo de Comunicação (protocol.py)

Tanto o cliente quanto o servidor utilizam um módulo de protocolo para padronizar a comunicação. Este módulo define mensagens estruturadas em JSON, garantindo interoperabilidade.

## Perguntas (server/questions/)

As perguntas do quiz são armazenadas em arquivos JSON, organizados por tema (ex.: technology.json, movies.json).

## Protocolo de Comunicação

O protocolo de comunicação foi implementado para garantir a interoperabilidade entre cliente e servidor. Ele utiliza mensagens no formato JSON, com os seguintes tipos principais:

### TYPE_QUESTION:

Enviado pelo servidor para o cliente, contendo uma pergunta e suas opções.

### TYPE_ANSWER:

Enviado pelo cliente para o servidor, contendo a resposta escolhida.

### TYPE_RESULT:

Enviado pelo servidor para o cliente, contendo a pontuação final.

Os tipos de mensagem e constantes utilizadas estão definidos no módulo protocol.py tanto no cliente quanto no servidor.

# Instruções de Uso

## Requisitos

### Python 3.8 ou superior

### Biblioteca padrão do Python (não são necessárias dependências externas)

## Passo a Passo

### Configuração do Servidor

Navegue até o diretório server/ e execute o servidor:

#### endereço: Endereço IP do servidor (padrão: localhost).

#### porta: Porta para escuta (padrão: 5000).

#### tema: Tema do quiz (ex.: technology, movies).

### Execução do Cliente

Navegue até o diretório client/ e execute o cliente:

#### endereço: Endereço IP do servidor.

#### porta: Porta para conexão.

## Interação

O cliente receberá perguntas do servidor, enviará respostas e exibirá a pontuação final.

# Padrão de Interoperabilidade

O projeto adota um protocolo baseado em JSON para garantir a interoperabilidade entre cliente e servidor. Este formato foi escolhido por sua simplicidade, legibilidade e ampla compatibilidade com diversas linguagens de programação. A estrutura modular do código permite que o protocolo seja facilmente adaptado para outras aplicações.
