from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def juntar_videos(video_paths, output_path="videos/final_video.mp4"):
    try:
        print("🔗 Juntando vídeos...")

        clips = [VideoFileClip(v) for v in video_paths]
        final = concatenate_videoclips(clips, method="compose")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        final.write_videofile(output_path, codec='libx264', audio_codec='aac')

        print(f"🎬 Vídeo final salvo em: {output_path}")
    except Exception as e:
        print(f"❌ Erro ao juntar vídeos: {e}")
