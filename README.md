# Skymail Security Alert Email Automation


## **Descrição**

O **Skymail Security Alert Email Automation** é uma solução em Python que automatiza o envio de notificações de segurança para clientes. A ferramenta:

- **Extrai** os e-mails dos colaboradores de um ticket de alerta (Exemplo 01).
- **Agrupa** esses e-mails por domínio (cada domínio representa um cliente).
- **Consulta** uma planilha Excel com os responsáveis de cada cliente.
- **Monta** e **envia** um e-mail com uma versão HTML enriquecida – com ícones e imagens – e um fallback em plain text.
- **Recomenda** gerenciadores de senhas, exibindo ícones e links para soluções como **LastPass**, **Bitwarden** e **1Password**.

---

## **Funcionalidades**

- **Extração Automática:** Utiliza expressões regulares para identificar os e-mails no relatório de segurança.
- **Agrupamento Inteligente:** Organiza os e-mails por domínio para facilitar o mapeamento com os responsáveis.
- **Integração com Excel:** Lê uma planilha (`responsaveis.xlsx`) que contém os dados dos responsáveis (Nome Fantasia, Razão Social e E-mail).
- **Envio de Notificações:** Envia e-mails via SMTP com um conteúdo visualmente atraente (HTML + plain text).
- **Recomendações de Segurança:** Inclui dicas com ícones para criar senhas fortes e recomenda gerenciadores de senhas.

---

## **Pré-requisitos**

Antes de utilizar este projeto, verifique se você possui:

- [Python 3.7+](https://www.python.org/downloads/)
- Bibliotecas Python:
  - **pandas**
  - **openpyxl**
  - **smtplib** (já incluída na biblioteca padrão)
  - **email** (módulo da biblioteca padrão)
- Acesso a um servidor SMTP (ex: Gmail, Outlook, etc.)
- Uma planilha Excel chamada **responsaveis.xlsx** com as colunas:
  - **Nome fantasia**
  - **Razão social**
  - **E-mail**

---

## **Como Funciona**

1. **Extração dos E-mails**  
   O script lê o corpo do código e utiliza uma expressão regular para identificar todos os endereços de e-mail.

2. **Agrupamento por Domínio**  
   Cada e-mail é agrupado com base no domínio (a parte após o `@`). Assim, é possível associar cada grupo a um cliente específico.
 
   *Os e-mails são organizados para facilitar o mapeamento com os responsáveis.*

3. **Consulta à Planilha de Responsáveis**  
   O script carrega a planilha `responsaveis.xlsx` e cria um mapeamento entre o domínio e o e-mail do responsável daquele cliente.

   *Certifique-se de que a planilha esteja no mesmo diretório do script.*

4. **Montagem e Envio do E-mail**  
   Para cada cliente, o script monta uma mensagem de alerta que inclui:
   - Versão **plain text** (fallback).
   - Versão **HTML** com elementos visuais, incluindo:
   
   *O e-mail é enviado automaticamente para os colaboradores (proprietários da conta de e-mail) e seus superiores (responsaveis.xlsx).*

---

## **Como Utilizar**

### **1. Configuração do Ambiente**

- **Clone o repositório:**

  ```bash
  git clone https://github.com/seu-usuario/skymail-security-alert-email-automation.git
  cd skymail-security-alert-email-automation
  
- **Instale as dependências:**

  ```bash
  pip install pandas openpyxl

 - ## 2. Configuração do Script

- **Abra o arquivo do script** (por exemplo, `envia_alerta_seguranca_email_responsaveis.py`).
- **Atualize as variáveis de configuração do SMTP:**
  - `SMTP_SERVER`
  - `SMTP_PORT`
  - `SMTP_USER`
  - `SMTP_PASSWORD`
- **Cole o conteúdo do ticket (Exemplo 01) na variável `conteudo_exemplo1`.**

## 3. Preparação da Planilha de Responsáveis

- **Crie um arquivo Excel chamado `responsaveis.xlsx` com as colunas:**
  - **Nome fantasia**
  - **Razão social**
  - **E-mail**
- **Preencha a planilha com os dados dos responsáveis dos clientes.**

## 4. Execução

- **Execute o script:**

  ```bash
  python envia_alerta_seguranca_email_responsaveis.py
- ## O script irá:

- **Extrair** os e-mails do ticket.
- **Agrupar** por domínio.
- **Consultar** a planilha para identificar os responsáveis.
- **Montar e enviar** o e-mail para os destinatários correspondentes.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests** para melhorar o projeto.
