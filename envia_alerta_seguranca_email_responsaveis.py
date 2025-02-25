import re
import smtplib
import pandas as pd
from email.message import EmailMessage
from collections import defaultdict

# ================= Configurações SMTP =====================
SMTP_SERVER   = "smtp.mail.net.br"           # Exemplo: smtp.gmail.com
SMTP_PORT     = 465                             # Porta SSL (ou 587 com starttls)
SMTP_USER     = "email@email.com"  # Seu e-mail
SMTP_PASSWORD = "password"                    # Sua senha ou app password
FROM_EMAIL    = SMTP_USER                       # Remetente
# ==========================================================

# =================== Templates de Email ===================

# Versão plain text (fallback)
PLAINTEXT_TEMPLATE = """Olá  {nome_cliente},

Você está recebendo uma notificação da área de segurança da Nmail.

Nosso sistema de segurança identificou que as seguintes contas (colaborador(es)) estão com senha de baixa complexidade (Senhas Fracas):
{lista_emails}

Para que a segurança dessas contas e dos nossos sistemas seja preservada, solicitamos que seja alterada para um padrão mais complexo.

Dicas para criar uma senha forte e segura:
- Tamanho: Use entre 10 e 15 caracteres.
- Variedade: Misture letras maiúsculas, minúsculas, números e símbolos especiais.
- Senhas distintas: Evite usar a mesma senha para diferentes contas.
- Nada óbvio: Não utilize informações pessoais, como datas de nascimento ou nomes.
- Teste de força: Utilize ferramentas como “How Secure Is My Password?” para avaliar sua nova senha.
- Gerenciador: Considere usar um gerenciador de senhas para criar e armazenar suas senhas com segurança.

Como alterar sua senha de e-mail:
1. Acesse seu e-mail e clique nos três pontinhos no canto inferior direito.
2. Selecione "Modificar Senha".
3. Digite sua senha atual, a nova senha duas vezes e clique em "Salvar".

Para mais informações, consulte nossa documentação:
https://sistema.nvirtual.com.br/kb/pt-br/article/376780/nmail-alterar-senha

Lembre-se dos requisitos para uma nova senha:
• Pelo menos 8 caracteres;
• Não incluir informações relacionadas ao seu e-mail;
• Evitar sequências numéricas ou alfabéticas (como "12345" ou "abcd");
• Incluir pelo menos um número e um caractere especial.

Caso não saiba a senha atual, entre em contato com nosso suporte para assistência.

Atenciosamente,
Equipe de Segurança Nmail.
"""

# Versão HTML
HTML_TEMPLATE = """\
<html>
  <body style="font-family: Arial, sans-serif; color: #333;">
    <div style="text-align: center; margin-bottom: 20px;">
      <img src="https://img.icons8.com/color/48/000000/security-checked.png" alt="Segurança" style="width:48px;height:48px;">
      <h2>Aviso de Segurança</h2>
    </div>
    <p>Olá <strong>{nome_cliente}</strong>,</p>
    <p>Você está recebendo uma notificação da área de segurança da <strong>Nmail</strong>.</p>
    <p>
      Nosso sistema de segurança identificou que as seguintes contas (colaborador(es)) estão com senha de baixa complexidade (Senhas Fracas):
    </p>
    <ul>
      {lista_emails_li}
    </ul>
    <p>
      Para que a segurança dessas contas e dos nossos sistemas seja preservada, solicitamos que seja alterada para um padrão mais complexo.
    </p>
    <h3>Dicas para criar uma senha forte e segura:</h3>
    <ul>
      <li>
        <img src="https://img.icons8.com/color/20/000000/lock.png" alt="Ícone" style="vertical-align: middle;">
        Tamanho: Use entre 10 e 15 caracteres.
      </li>
      <li>
        <img src="https://img.icons8.com/color/20/000000/lock.png" alt="Ícone" style="vertical-align: middle;">
        Variedade: Misture letras maiúsculas, minúsculas, números e símbolos especiais.
      </li>
      <li>
        <img src="https://img.icons8.com/color/20/000000/lock.png" alt="Ícone" style="vertical-align: middle;">
        Senhas distintas: Evite usar a mesma senha para diferentes contas.
      </li>
      <li>
        <img src="https://img.icons8.com/color/20/000000/lock.png" alt="Ícone" style="vertical-align: middle;">
        Nada óbvio: Não utilize informações pessoais, como datas de nascimento ou nomes.
      </li>
      <li>
        <img src="https://img.icons8.com/color/20/000000/lock.png" alt="Ícone" style="vertical-align: middle;">
        Teste de força: Utilize ferramentas para teste de senha e escreva sua senha em <a href="https://www.security.org/how-secure-is-my-password/" target="_blank">“How Secure Is My Password?”</a> para avaliar sua nova senha. Caso sua Senha fique Verde se trata de uma senha segura.
      </li>
      <li>
      <img src="https://img.icons8.com/color/20/000000/lock.png" alt="Ícone de segurança" style="vertical-align: middle; margin-right: 5px;">
      Gerenciador: Considere usar um gerenciador de senhas para criar e armazenar suas senhas com segurança.
      Recomendamos 
      <img src="https://img.icons8.com/color/20/000000/lastpass.png" alt="LastPass" style="vertical-align: middle; margin: 0 5px;">
      <a href="https://www.lastpass.com/pt" target="_blank">LastPass</a>,
      <img src="https://img.icons8.com/color/20/000000/bitwarden.png" alt="Bitwarden" style="vertical-align: middle; margin: 0 5px;">
      <a href="https://bitwarden.com/" target="_blank">Bitwarden</a> ou 
      <img src="https://img.icons8.com/color/20/000000/1password.png" alt="1Password" style="vertical-align: middle; margin: 0 5px;">
      <a href="https://1password.com/" target="_blank">1Password</a>
    </li>
      <li>
        <img src="https://img.icons8.com/color/20/000000/lock.png" alt="Ícone" style="vertical-align: middle;">
        Se sente sem criatividade? Utilize ferramentas para criar senhas automaticamente <a href="https://www.keepersecurity.com/pt_BR/features/password-generator.html" target="_blank">“Clicando Aqui”</a> e guarde-a de forma segura.
      </li>
    </ul>
    <h3>Como alterar sua senha de e-mail:</h3>
    <ol>
      <li>Acesse seu e-mail e clique nos três pontinhos no canto inferior direito.</li>
      <li>Selecione <strong>Modificar Senha</strong>.</li>
      <li>Digite sua senha atual, a nova senha duas vezes e clique em <strong>Salvar</strong>.</li>
    </ol>
    <p>
      Para mais informações, consulte nossa <a href="https://sistema.nvirtual.com.br/kb/pt-br/article/376780/nmail-alterar-senha" target="_blank">documentação</a>.
    </p>
    <p>
      Lembre-se dos requisitos para uma nova senha:<br>
      • Pelo menos 8 caracteres;<br>
      • Não incluir informações relacionadas ao seu e-mail;<br>
      • Evitar sequências numéricas ou alfabéticas (como "12345" ou "abcd");<br>
      • Incluir pelo menos um número e um caractere especial.
    </p>
    <p>
      Caso não saiba a senha atual, entre em contato com nosso suporte para assistência.
    </p>
    <p>
      Atenciosamente,<br>
      Equipe de Segurança Nmail.
    </p>
  </body>
</html>
"""

# ================= Funções Auxiliares =====================

def extrair_emails(texto):
    """
    Extrai todos os e-mails do texto utilizando regex.
    """
    padrao = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(padrao, texto)

def agrupar_por_dominio(emails):
    """
    Agrupa os e-mails por domínio (parte após o @).
    Retorna um dicionário com chave = domínio e valor = lista de e-mails.
    """
    grupos = defaultdict(list)
    for email in emails:
        dominio = email.split('@')[1].lower()
        grupos[dominio].append(email)
    return grupos

def montar_mensagem_text(nome_cliente, lista_emails):
    """
    Monta a mensagem na versão plain text.
    """
    emails_formatados = "\n".join(lista_emails)
    return PLAINTEXT_TEMPLATE.format(nome_cliente=nome_cliente.capitalize(), lista_emails=emails_formatados)

def montar_mensagem_html(nome_cliente, lista_emails):
    """
    Monta a mensagem na versão HTML com ícones e imagens.
    """
    lista_emails_li = "".join(f"<li>{email}</li>" for email in lista_emails)
    return HTML_TEMPLATE.format(nome_cliente=nome_cliente.capitalize(), lista_emails_li=lista_emails_li)

def enviar_email(destinatarios, assunto, texto_plano, html_corpo):
    """
    Envia o e-mail utilizando SMTP com versões plain text e HTML.
    destinatarios: lista de e-mails (colaboradores e responsáveis)
    """
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = FROM_EMAIL
    msg['To'] = ", ".join(destinatarios)
    
    # Define a versão plain text (fallback)
    msg.set_content(texto_plano)
    # Adiciona a versão HTML
    msg.add_alternative(html_corpo, subtype='html')
    
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        print(f"E-mail enviado para: {msg['To']}")
    except Exception as e:
        print(f"Erro ao enviar e-mail para {msg['To']}: {e}")

def carregar_responsaveis(arquivo):
    """
    Carrega a planilha de responsáveis a partir de um arquivo Excel.
    A planilha deve conter as colunas: "Nome fantasia", "Razão social" e "E-mail".
    Cria um dicionário com chave = domínio (extraído do e-mail do responsável)
    e valor = lista de e-mails dos responsáveis daquele domínio.
    """
    try:
        df = pd.read_excel(arquivo)
        responsaveis = {}
        for _, row in df.iterrows():
            email_resp = str(row['E-mail']).strip()
            if email_resp:
                try:
                    domain = email_resp.split('@')[1].lower()
                except IndexError:
                    continue
                if domain not in responsaveis:
                    responsaveis[domain] = set()
                responsaveis[domain].add(email_resp)
        # Converte os sets para listas
        responsaveis = {dom: list(emails) for dom, emails in responsaveis.items()}
        return responsaveis
    except Exception as e:
        print("Erro ao carregar a planilha de responsáveis:", e)
        return {}

# ===================== Função Principal ====================

def main():
    # --- Conteúdo copiado do Exemplo 01 ---
    conteudo_exemplo1 = """
--------------------------------------------------------------------------------------------------------------------
!!!COLOQUE A LISTA DE EMAILS COM SENHA FRACA AQUI!!!
paulomatheus@nvirtual.com.br
--------------------------------------------------------------------------------------------------------------------
"""
    # --- Fim do conteúdo do Exemplo 01 ---

    # Carrega os responsáveis a partir da planilha (arquivo responsaveis.xlsx)
    responsaveis_mapping = carregar_responsaveis("responsaveis.xlsx")
    if not responsaveis_mapping:
        print("Nenhum responsável foi carregado. Verifique a planilha.")
    
    # Extrai os e-mails do conteúdo
    emails_extraidos = extrair_emails(conteudo_exemplo1)
    if not emails_extraidos:
        print("Nenhum e-mail foi encontrado no conteúdo fornecido.")
        return

    # Agrupa os e-mails dos colaboradores por domínio
    grupos = agrupar_por_dominio(emails_extraidos)
    
    # Para cada domínio (cliente), monta e envia o e-mail
    for dominio, lista_emails in grupos.items():
        # Para exibir o nome do cliente na mensagem, podemos usar o domínio (ex.: "sumireonline.com.br")
        nome_cliente = dominio
        
        # Busca os responsáveis para este domínio, se houver na planilha
        responsaveis_emails = responsaveis_mapping.get(dominio, [])
        if not responsaveis_emails:
            print(f"Responsável não encontrado para o domínio '{dominio}'. Enviando somente para os colaboradores.")
            destinatarios = lista_emails
        else:
            # Junta os e-mails dos colaboradores com os responsáveis, eliminando duplicatas
            destinatarios = list(set(lista_emails + responsaveis_emails))
        
        # Monta as versões do e-mail
        texto_plano = montar_mensagem_text(nome_cliente, lista_emails)
        html_corpo = montar_mensagem_html(nome_cliente, lista_emails)
        assunto = "Aviso de Segurança"
        
        # Envia o e-mail
        enviar_email(destinatarios, assunto, texto_plano, html_corpo)

if __name__ == "__main__":
    main()
