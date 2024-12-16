import yt_dlp
import os

def baixar_audio_em_mp3(url, destino="./"):
    try:
        # Configuração das opções para o yt_dlp
        opcoes = {
            "format": "bestaudio/best",  # Seleciona o melhor áudio disponível
            "outtmpl": os.path.join(destino, "%(title)s.%(ext)s"),  # Nome do arquivo de saída
            "postprocessors": [
                {  # Converte para MP3 após o download
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",  # Qualidade do MP3 (kbps)
                }
            ],
        }

        # Baixar o áudio usando yt_dlp
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            print(f"Baixando áudio de: {url}")
            ydl.download([url])
        print("Download concluído com sucesso!")

    except Exception as e:
        print(f"Erro ao baixar o áudio: {e}")

# Solicitar URL do vídeo e caminho de destino
url_video = input("Insira a URL do vídeo do YouTube: ")
destino_pasta = input("Insira o caminho de destino (deixe vazio para o diretório atual): ") or "./"

# Certificar-se de que o destino existe
if not os.path.exists(destino_pasta):
    os.makedirs(destino_pasta)

baixar_audio_em_mp3(url_video, destino_pasta)