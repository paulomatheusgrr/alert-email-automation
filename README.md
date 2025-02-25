# Skymail Security Alert Email Automation

## **Portuguese Version:**
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

---
---
## **English Version**


## **Description**

The **Skymail Security Alert Email Automation** is a Python solution that automates the sending of security notifications to clients. The tool:

- **Extracts** employee emails from a security alert ticket (Example 01).
- **Groups** these emails by domain (each domain represents a client).
- **Consults** an Excel spreadsheet containing each client's responsible party.
- **Composes** and **sends** an email with an enriched HTML version – featuring icons and images – with a plain text fallback.
- **Recommends** password managers by displaying icons and links for solutions such as **LastPass**, **Bitwarden**, and **1Password**.

---

## **Features**

- **Automatic Email Extraction:** Uses regular expressions to identify emails in the security report.
- **Intelligent Grouping:** Organizes emails by domain to facilitate mapping with the responsible parties.
- **Excel Integration:** Reads an Excel spreadsheet (`responsaveis.xlsx`) containing responsible parties’ data (Trading Name, Legal Name, and Email).
- **Notification Sending:** Sends emails via SMTP with visually appealing content (HTML + plain text).
- **Security Recommendations:** Includes tips with icons for creating strong passwords and recommends password managers.

---

## **Prerequisites**

Before using this project, ensure you have:

- [Python 3.7+](https://www.python.org/downloads/)
- Python libraries:
  - **pandas**
  - **openpyxl**
  - **smtplib** (included in the standard library)
  - **email** (module from the standard library)
- Access to an SMTP server (e.g., Gmail, Outlook, etc.)
- An Excel spreadsheet named **responsaveis.xlsx** with the columns:
  - **Trading Name**
  - **Legal Name**
  - **Email**

---

## **How It Works**

1. **Email Extraction**  
   The script reads the content of the ticket and uses a regular expression to identify all email addresses.

2. **Domain Grouping**  
   Each email is grouped based on its domain (the part after the `@`). This way, each group can be associated with a specific client.  
   *Emails are organized to facilitate mapping with the responsible parties.*

3. **Responsible Party Lookup**  
   The script loads the `responsaveis.xlsx` spreadsheet and creates a mapping between the domain and the responsible party's email for that client.  
   *Ensure that the spreadsheet is in the same directory as the script.*

4. **Email Composition and Sending**  
   For each client, the script composes an alert message that includes:
   - A **plain text** version (fallback).
   - An **HTML** version with visual elements.  
   
   *The email is automatically sent to the employees (owners of the email account) and their superiors (as listed in responsaveis.xlsx).*

---

## **How to Use**

### **1. Environment Setup**

- **Clone the repository:**

  ```bash
  git clone https://github.com/your-username/skymail-security-alert-email-automation.git
  cd skymail-security-alert-email-automation
  ```

- **Install dependencies:**

  ```bash
  pip install pandas openpyxl
  ```

### **2. Script Configuration**

- **Open the script file** (for example, `envia_alerta_seguranca_email_responsaveis.py`).
- **Update the SMTP configuration variables:**
  - `SMTP_SERVER`
  - `SMTP_PORT`
  - `SMTP_USER`
  - `SMTP_PASSWORD`
- **Paste the ticket content (Example 01) into the variable `conteudo_exemplo1`.**

### **3. Prepare the Responsible Parties Spreadsheet**

- **Create an Excel file named `responsaveis.xlsx` with the columns:**
  - **Trading Name**
  - **Legal Name**
  - **Email**
- **Fill in the spreadsheet with the data of each client's responsible party.**

### **4. Execution**

- **Run the script:**

  ```bash
  python envia_alerta_seguranca_email_responsaveis.py
  ```

- **The script will:**
  - **Extract** the emails from the ticket.
  - **Group** them by domain.
  - **Consult** the spreadsheet to identify the responsible parties.
  - **Compose and send** the email to the corresponding recipients.

---

## **Contribution**

Contributions are welcome! Feel free to open **issues** or submit **pull requests** to improve the project.
