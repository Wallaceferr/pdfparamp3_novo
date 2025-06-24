import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog
import pygame
import threading

# Função para extrair texto de um arquivo PDF
def extraindo_texto_do_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

# Função para converter texto em fala e salvar como arquivo MP3
def play_no_texto(text, pdf_name):
    tts = gTTS(text, lang='pt-BR', slow=False, tld='com.br')
    audio_file_name = pdf_name.replace('.pdf', '.mp3')
    tts.save(audio_file_name)
    return audio_file_name

# Função para tocar o áudio
def play_audio(audio_file):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    info_label.config(text=f"Reproduzindo áudio: {audio_file}")

# Função que lida com o botão "Carregar PDF"
def carregar_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_path:
        info_label.config(text="Processando PDF...")
        iniciar_processamento(pdf_path)

# Função que lida com o botão "Reproduzir Áudio"
def reproduzir_audio():
    audio_file_name = info_label.cget("text").split(": ")[1]
    play_audio(audio_file_name)

# Função para processar o PDF em segundo plano
def processar_pdf(pdf_path):
    text = extraindo_texto_do_pdf(pdf_path)
    audio_file_name = play_no_texto(text, os.path.basename(pdf_path))
    info_label.config(text=f'Arquivo de MP3 gerado: {audio_file_name}')
    play_button.config(state=tk.NORMAL)

# Função para iniciar o processamento em segundo plano
def iniciar_processamento(pdf_path):
    processing_thread = threading.Thread(target=processar_pdf, args=(pdf_path,))
    processing_thread.start()

# Janela Tkinter
root = tk.Tk()
root.title("PDF para MP3")

# Criação e posicionamento dos widgets
load_button = tk.Button(root, text="Carregar PDF", command=carregar_pdf)
load_button.pack(pady=10)

info_label = tk.Label(root, text="", wraplength=400)
info_label.pack()

play_button = tk.Button(root, text="Reproduzir Áudio", command=reproduzir_audio, state=tk.DISABLED)
play_button.pack(pady=10)

# Inicia o loop principal da Interface
root.mainloop()
