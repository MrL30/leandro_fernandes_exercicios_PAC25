# Sistema de Chat Multi-Utilizador (GDPR & Engenharia Social)

**Laboratório 1 - Sistema de Chat com Deteção de Dados Pessoais e Engenharia Social**

Este projeto implementa um sistema de chat cliente-servidor em Python, focado na comunicação em tempo real e na segurança dos utilizadores. O sistema garante a conformidade com o Regulamento Geral sobre a Proteção de Dados (RGPD/GDPR) ao bloquear a partilha de dados sensíveis, e inclui um módulo avançado para a deteção de padrões de Engenharia Social.

---

## Funcionalidades Principais

Multi-utilizador em Tempo Real: Suporte para múltiplos clientes em simultâneo através da utilização das bibliotecas `threading` e `sockets`.

Filtro GDPR Ativo: Interceção e bloqueio automático de mensagens que contenham emails, números de telemóvel/telefone, nomes reais ou passwords, utilizando Expressões Regulares (Regex).

Módulo de Engenharia Social (Extra): Avaliação de risco comportamental em tempo real. O servidor analisa gatilhos de urgência ou pressão psicológica e atribui um "Score de Risco" a cada utilizador.

Auditoria e Logs: Registo detalhado e seguro de todas as tentativas de engenharia social num ficheiro `auditoria_scores.txt` e alertas de segurança num ficheiro `logs_gdpr.txt`.

Comandos Especiais: Suporte para comandos de terminal intuitivos (ex.: `exit` para sair da sala e `/status` para consultar o próprio risco de segurança).

---

## Tecnologias e Arquitetura

O projeto foi desenvolvido inteiramente em Python 3 e baseia-se numa arquitetura centralizada do tipo  Cliente-Servidor .

* Servidor (`servidor.py`): Atua como o nó central. Gere as ligações recebidas através de threads dedicadas, garantindo que as mensagens processadas não bloqueiam a experiência dos restantes utilizadores. É aqui que reside a lógica principal: auditoria de mensagens, verificação de regex e a gravação de logs de segurança.
* Cliente (`cliente.py`): Interface de Linha de Comandos (CLI) simples e fluida. Possui threads separadas para garantir que o envio e a receção de mensagens ocorrem em simultâneo e sem interrupções na escrita do utilizador.

---

## Pré-Requisitos e Instalação

Antes de executar o projeto, certifique-se de que tem o Python 3.x instalado na sua máquina.

Dependências:
Não são necessárias bibliotecas externas. O projeto funciona inteiramente com as bibliotecas *built-in* do Python (`socket`, `threading`, `re`, `os`).

---

## Como Executar o Projeto

O sistema deve ser iniciado numa ordem específica para garantir que a ligação cliente-servidor não falha.

### Passo 1: Iniciar o Servidor

Abra o seu terminal (ou linha de comandos), navegue até à pasta do projeto e execute o servidor:

```
python servidor.py
```

O servidor ficará à escuta de ligações no endereço local `127.0.0.1` e na porta `12340`.

### Passo 2: Iniciar os Clientes

Abra novas janelas de terminal para cada utilizador que queira simular e execute o ficheiro do cliente:

```
python cliente.py
```

1. Introduza o seu nome de utilizador quando solicitado pelo terminal.
2. Comece a conversar com os outros utilizadores na sala.

---

## Guia de Utilização (Comandos do Chat)

Durante a conversa na interface do cliente, pode interagir de diferentes formas:

Mensagem Normal: Escreva texto livremente e prima Enter. Se o texto contiver dados sensíveis (ex.: `o meu email é teste@teste.com`), a mensagem será bloqueada pelo servidor e não chegará aos outros utilizadores.

`/status`: Um comando especial que consulta o servidor e lhe devolve o seu nível de risco atual, baseado no seu comportamento e vocabulário na sala.

`sair`: Desliga a sua ligação de forma segura do servidor e emite um aviso aos restantes participantes de que saíu do chat.

---

## Estrutura de Ficheiros

```
/
├── servidor.py         # Código principal do servidor (Lógica GDPR e Ligações)
├── cliente1.py         # Interface do utilizador1 para envio/receção de mensagens
├── cliente2.py         # Interface do utilizador2 para envio/receção de mensagens
├── cliente3.py         # Interface do utilizador3 para envio/receção de mensagens
├── README.md           # Documentação do projeto
└── logs/               # Pasta gerada automaticamente pelo servidor
    ├── auditoria_scores.txt  # Logs de tentativas de engenharia social
    └── logs_gdrp.txt         # Logs de infrações cometidas
```
