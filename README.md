# Desafio Login

Este projeto é um sistema de autenticação desenvolvido em Django, permitindo login e registro de usuários.

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Django**
- **SQLite**
- **Bootstrap** (Para estilização do frontend)

## 📌 Funcionalidades
- Registro de usuários com e-mail e senha
- Login e Logout de usuários
- Sistema de permissões e restrição de acesso

## 🔧 Como Configurar o Projeto


### 3️⃣ Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar as Variáveis de Ambiente
⚠️ Comportamento de Envio de E-mail
Quando DEBUG=True, o Django usará o backend django.core.mail.backends.console.EmailBackend. Nesse modo, os e-mails de confirmação e outros serão exibidos no console (não são enviados de fato).

Quando DEBUG=False, você precisará configurar um servidor de e-mail real. Se for configurado corretamente, os e-mails serão enviados de fato.
```env
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "SeuEmail@gmail.com"
EMAIL_HOST_PASSWORD="Sua Senha"
```


### 5️⃣ Aplicar as Migrações do Banco de Dados
```bash
python manage.py migrate
```

### 7️⃣ Rodar o Servidor
```bash
python manage.py runserver
```
Acesse a aplicação em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📜 Endpoints Principais
- `/admin/` → Painel de administração do Django
- `/` → Página de login
- `/register/` → Página de registro (envia um e-mail de confirmação no modo teste, que aparece no console)
- `/menu/` → Página principal após login
- `/logout/` → Rota para logout



