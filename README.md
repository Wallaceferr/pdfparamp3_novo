# PDF para MP3

Este projeto é um sistema desktop que permite a conversão de textos contidos em arquivos PDF para áudio (formato MP3), promovendo acessibilidade para pessoas com deficiência visual, dificuldades de leitura ou até mesmo para quem deseja ouvir conteúdos acadêmicos ou profissionais enquanto realiza outras tarefas.

## 🧠 Objetivo

Desenvolver uma aplicação que facilite o acesso a conteúdos escritos por meio da conversão de arquivos PDF em arquivos de áudio, utilizando bibliotecas Python como `PyPDF2`, `gTTS` e `pygame`.

## 📌 Funcionalidades

- Interface gráfica simples e intuitiva (Tkinter)
- Extração automática de texto de arquivos PDF
- Conversão do texto para áudio com o Google Text-to-Speech (gTTS)
- Reprodução do áudio na própria aplicação
- Processamento em segundo plano com `threading`

## 💡 Motivação

Segundo a Pesquisa Nacional de Saúde (PNS - 2019), cerca de 3,4% da população brasileira possui alguma deficiência visual. Quando ampliamos esse número para pessoas com dislexia ou dificuldades cognitivas, esse percentual pode chegar até 15% da população mundial, segundo a International Dyslexia Association (IDA). Esta aplicação visa atender esse público, além de auxiliar estudantes e profissionais que desejam ouvir textos durante outras atividades.

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – Interface gráfica
- [PyPDF2](https://pypi.org/project/PyPDF2/) – Leitura de arquivos PDF
- [gTTS](https://pypi.org/project/gTTS/) – Conversão de texto para áudio (requer conexão com a internet)
- [pygame](https://pypi.org/project/pygame/) – Reprodução de arquivos de áudio
- [threading](https://docs.python.org/3/library/threading.html) – Execução paralela de tarefas

## ▶️ Como executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Wallaceferr/pdfparamp3_novo.git
   cd pdfparamp3_novo
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o sistema**
   ```bash
   python main.py
   ```

## 📈 Resultados do projeto

O sistema foi testado com usuários reais e obteve avaliações muito positivas em termos de usabilidade, qualidade do áudio e funcionalidade.

## 📦 Futuras melhorias

- Adição de barra de progresso durante o processamento
- Botão de parar áudio
- Mensagens de alerta com `messagebox`
- Versão web responsiva
- Suporte para múltiplos idiomas

## 📄 Artigo

Este projeto foi desenvolvido como parte do Trabalho de Conclusão de Curso (TCC).

Você pode acessar o artigo completo clicando no link abaixo:

🔗 [Leia o artigo completo do TCC (PDF)](./docs/artigo_tcc_wallace_versaofinal.pdf)

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 👤 Autor

**Wallace Ferreira**  
[GitHub](https://github.com/Wallaceferr)
