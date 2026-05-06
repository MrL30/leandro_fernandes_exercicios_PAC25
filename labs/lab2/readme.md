# Documentação do Projeto: Web Crawler Bot

## Descrição

Este projeto consiste num rastreador web (Web Crawler) desenvolvido em Python, concebido para mapear a estrutura de ligações de domínios específicos. O script realiza a extração de metadados, identifica relações entre páginas e organiza os dados em ficheiros estruturados, operando de acordo com as boas práticas de web scraping e polidez de rede.

## Funcionalidades Técnicas

* **Conformidade com o Robots.txt** : Integração com a biblioteca `urllib.robotparser` para validar as permissões de acesso antes de processar qualquer URL.
* **Gestão de Fila (BFS)** : Implementação de lógica de exploração em largura para garantir uma navegação estruturada.
* **Tratamento de Exceções** : Gestão robusta de erros de ligação, interrupções de tempo (timeouts) de 5 segundos e códigos de estado HTTP (4xx e 5xx).
* **Persistência de Dados** : Sistema de escrita automática em formato JSON, com suporte para interrupção segura através do teclado (SIGINT).
* **Simulação de Comportamento Humano** : Introdução de intervalos (delays) aleatórios entre 1.0 e 2.5 segundos para evitar a sobrecarga dos servidores e eventuais bloqueios de IP.

## Requisitos de Instalação

O projeto requer Python 3.x e as seguintes dependências externas:

**Bash**

```
pip install requests beautifulsoup4
```

## Instruções de Utilização

1. Execute o ficheiro principal:

   ```
   python crawler.py
   ```
2. Introduza o URL inicial completo (incluindo o protocolo http/https).
3. Defina o limite de navegação:

   * **Valor numérico** : Limita a exploração ao número de páginas indicado.
   * **'tudo'** : Ativa o modo de mapeamento exaustivo sem limite definido.

## Estrutura de Saída

Os resultados são armazenados numa diretoria criada dinamicamente com base no nome do domínio visado. São gerados três ficheiros fundamentais:

* **crawler_sucesso.json** : Registo de todas as páginas processadas com êxito, incluindo os títulos das páginas e a lista de ligações extraídas.
* **crawler_erros.json** : Registo detalhado de URLs que devolveram erros de HTTP ou falhas de conectividade.
* **crawler_grafico.json** : Representação em formato de grafo das ligações entre as diferentes páginas do domínio.

## Especificações do User-Agent

O crawler identifica-se através do User-Agent `MrL30`. Esta configuração pode ser personalizada diretamente no cabeçalho da função principal do código para cumprir requisitos específicos de identificação.

## Aviso Legal

Esta ferramenta deve ser utilizada exclusivamente para fins académicos ou de análise técnica autorizada. O utilizador é o único responsável por garantir que a atividade de rastreio está em conformidade com os Termos de Serviço do sítio web visado e com a legislação de proteção de dados em vigor.
