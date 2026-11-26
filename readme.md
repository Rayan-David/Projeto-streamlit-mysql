# 🍎 Sistema de Cadastro de Hortifrúti

Aplicação web desenvolvida em **Python** com **Streamlit** e integrada a um banco de dados **MySQL** para o cadastro e gerenciamento de produtos de um hortifrúti.

---

## 📋 Funcionalidades

- **Interface Web Interativa:** Formulário limpo e responsivo construído com Streamlit.
- **Categorização de Produtos:** Seleção predefinida entre *Frutas*, *Verduras* e *Legumes*.
- **Validação de Entrada:** Verificação obrigatória do campo *Nome do Produto* antes do envio ao banco, exibindo alertas visuais ao usuário.
- **Persistência em Banco de Dados:** Inserção segura de registros no MySQL utilizando consultas parametrizadas (`%s`) para prevenção contra *SQL Injection*.
- **Segurança e Controle de Acesso:** Script SQL configurado com usuário dedicado (`app_hortifruti`) e privilégios restritos apenas às operações necessárias (`SELECT` e `INSERT`).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Interface Web:** [Streamlit](https://streamlit.io/)
- **Banco de Dados:** MySQL
- **Conector / Bibliotecas:** `mysql-connector-python`, `pandas`

---

## 📂 Estrutura do Projeto

```text
PY+BD/
├── app.py          # Interface web (Streamlit) e regras de validação do formulário
├── banco.py        # Módulo de conexão com o MySQL e execução de queries
├── hortifruti.sql  # Script de criação do banco, tabela e usuário com permissões
└── README.md       # Documentação do projeto
```

---

## 🗄️ Estrutura do Banco de Dados

O script `hortifruti.sql` cria o banco de dados `hortifruti` e a tabela `produto` com a seguinte estrutura:

| Coluna | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `INT` | `PRIMARY KEY`, `AUTO_INCREMENT`, `NOT NULL` | Identificador único do produto |
| `nome` | `VARCHAR(50)` | `NOT NULL` | Nome do produto cadastrado |
| `categoria` | `VARCHAR(20)` | `NOT NULL` | Categoria (*Frutas*, *Verduras* ou *Legumes*) |
| `preco` | `DECIMAL(7,2)` | `NOT NULL` | Preço unitário em Reais (R$) |

---

## 🚀 Como executar o projeto

### Pré-requisitos
- [Python 3.12](https://www.python.org/) ou superior instalado.
- Servidor [MySQL](https://www.mysql.com/) ativo em `localhost`.

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Rayan-David/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Instale as dependências Python:**
   ```bash
   pip install streamlit mysql-connector-python pandas
   ```

3. **Configure o Banco de Dados MySQL:**
   Execute o arquivo `hortifruti.sql` no seu cliente MySQL (MySQL Workbench, terminal, DBeaver, etc.) para criar o banco `hortifruti`, a tabela `produto` e o usuário `app_hortifruti`:
   ```bash
   mysql -u root -p < hortifruti.sql
   ```

4. **Execute a aplicação Streamlit:**
   ```bash
   streamlit run app.py
   ```

5. **Acesse no navegador:**
   O sistema abrirá automaticamente no endereço local (geralmente `http://localhost:8501`).

---

## 🔒 Observação de Segurança

Para ambientes de produção ou repositórios públicos, recomenda-se mover as credenciais de acesso do arquivo `banco.py` (`user` e `password`) para variáveis de ambiente (`.env` ou `st.secrets` do Streamlit) em vez de mantê-las diretamente no código-fonte.

---

## 👤 Autor

Desenvolvido por **Rayan David**
- [GitHub](https://github.com/Rayan-David)