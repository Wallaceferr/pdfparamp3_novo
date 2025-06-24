import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
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
    stop_button.config(state=tk.NORMAL)

# Função para parar o áudio
def parar_audio():
    pygame.mixer.music.stop()
    stop_button.config(state=tk.DISABLED)
    messagebox.showinfo("Áudio", "Reprodução de áudio interrompida.")

# Função que lida com o botão "Carregar PDF"
def carregar_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if pdf_path:
        info_label.config(text="Processando PDF...")
        progress_bar['value'] = 10
        iniciar_processamento(pdf_path)

# Função que lida com o botão "Reproduzir Áudio"
def reproduzir_audio():
    try:
        audio_file_name = info_label.cget("text").split(": ")[1]
        info_label.config(text=f"Reproduzindo áudio: {audio_file_name}")
        progress_bar['value'] = 100
        play_audio(audio_file_name)
    except IndexError:
        messagebox.showwarning("Aviso", "Nenhum arquivo de áudio disponível. Carregue um PDF primeiro.")

# Função para processar o PDF em segundo plano
def processar_pdf(pdf_path):
    try:
        progress_bar['value'] = 20
        text = extraindo_texto_do_pdf(pdf_path)
        progress_bar['value'] = 60
        audio_file_name = play_no_texto(text, os.path.basename(pdf_path))
        progress_bar['value'] = 90
        info_label.config(text=f'Arquivo de MP3 gerado: {audio_file_name}')
        play_button.config(state=tk.NORMAL)
        messagebox.showinfo("Sucesso", "Áudio gerado com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Função para iniciar o processamento em segundo plano
def iniciar_processamento(pdf_path):
    processing_thread = threading.Thread(target=processar_pdf, args=(pdf_path,))
    processing_thread.start()

# Janela Tkinter
root = tk.Tk()
root.title("PDF para MP3")
root.geometry("500x200")

# Criação e posicionamento dos widgets
load_button = tk.Button(root, text="Carregar PDF", command=carregar_pdf)
load_button.pack(pady=10)

info_label = tk.Label(root, text="", wraplength=450)
info_label.pack()

play_button = tk.Button(root, text="Reproduzir Áudio", command=reproduzir_audio, state=tk.DISABLED)
play_button.pack(pady=10)

stop_button = tk.Button(root, text="Parar Áudio", command=parar_audio, state=tk.DISABLED)
stop_button.pack(pady=5)

progress_bar = tk.ttk.Progressbar(root, orient="horizontal", mode="determinate", length=400)
progress_bar.pack(pady=10)

# Inicia o loop principal da Interface
root.mainloop()