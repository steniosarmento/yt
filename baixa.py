import yt_dlp as youtube_dl

def baixar_video(url):
    try:
        # Definir as opções de download
        ydl_opts = {
            'format': 'bestvideo[ext=mp4][vcodec^=avc1][height<=720]+bestaudio[ext=m4a]/best[ext=mp4]',  # Vídeo com codec H.264 (avc1) e áudio AAC
            'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo será o título do vídeo
            'merge_output_format': 'mp4',  # Mesclar vídeo e áudio no formato MP4
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Converter para MP4 se necessário
            }],
            'postprocessor_args': [
                '-vf', 'scale=720:trunc(ow/a/2)*2',  # Limitar a resolução a 720p
                '-c:v', 'libx264',  # Usar o codec de vídeo H.264
                '-c:a', 'aac',  # Usar o codec de áudio AAC
                '-strict', 'experimental',  # Habilitar o uso do codec AAC se necessário
                '-b:a', '128k',  # Limitar o bitrate do áudio a 128 kbps
            ],
        }

        # Baixar o vídeo com yt-dlp
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download completo!")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# URL do vídeo do YouTube
url_video = input("Digite a URL do vídeo do YouTube: ")

# Chamar a função para baixar o vídeo
baixar_video(url_video)