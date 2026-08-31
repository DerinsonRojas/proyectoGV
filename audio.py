import yt_dlp

def descargar_mp3(url_youtube, nombre_salida="cancion"):
    opciones = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', # Calidad de audio (kbps)
        }],
        'outtmpl': nombre_salida, # Nombre del archivo final (sin extensión)
    }

    print(f"Descargando y convirtiendo el audio de: {url_youtube}...")
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url_youtube])
    print(f"¡Listo! Archivo guardado como {nombre_salida}.mp3")


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=RhBiKO14xbU"
    descargar_mp3(url, "cancion")