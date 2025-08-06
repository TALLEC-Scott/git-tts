import os
import sys
import soundfile as sf
import subprocess
from kittentts import KittenTTS

def play_audio(filename):
    """Play audio file using system audio player"""
    try:
        if os.name == 'nt':  # Windows
            os.startfile(filename)
        elif sys.platform == 'darwin':  # macOS
            subprocess.run(['open', filename])
        else:  # Linux/WSL
            players = ['paplay', 'aplay']
            for player in players:
                try:
                    subprocess.run([player, filename], check=True, stderr=subprocess.DEVNULL)
                    print(f"Audio played using {player}")
                    return
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
            raise Exception("No audio player found")
    except Exception as e:
        print(f"Could not play audio: {e}")
        print(f"Audio saved as: {filename}")

def main():
    print("KittenTTS Terminal Interface")
    print("Available voices: expr-voice-2-m, expr-voice-2-f, expr-voice-3-m, expr-voice-3-f, expr-voice-4-m, expr-voice-4-f, expr-voice-5-m, expr-voice-5-f")
    print("Type 'quit' to exit\n")

    # Initialize TTS model
    print("Loading TTS model...")
    tts = KittenTTS("KittenML/kitten-tts-nano-0.1")
    print("Model loaded!\n")

    voice = 'expr-voice-2-m'  # Default voice

    while True:
        # Get text input
        text = input("Enter text to speak (or 'voice:<voice-name>' to change voice): ").strip() + ".!"

        if text.lower() == 'quit':
            print("Goodbye!")
            break

        if text.startswith('voice:'):
            new_voice = text.split(':', 1)[1].strip()
            if new_voice in ['expr-voice-2-m', 'expr-voice-2-f', 'expr-voice-3-m', 'expr-voice-3-f', 'expr-voice-4-m', 'expr-voice-4-f', 'expr-voice-5-m', 'expr-voice-5-f']:
                voice = new_voice
                print(f"Voice changed to: {voice}")
            else:
                print("Invalid voice. Available voices: expr-voice-2-m, expr-voice-2-f, expr-voice-3-m, expr-voice-3-f, expr-voice-4-m, expr-voice-4-f, expr-voice-5-m, expr-voice-5-f")
            continue

        if not text:
            continue

        try:
            print(f"Generating speech with voice '{voice}'...")
            audio = tts.generate(text, voice=voice)

            filename = 'output.wav'
            sf.write(filename, audio, 24000)
            print(f"Audio generated: {filename}")

            play_audio(filename)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

