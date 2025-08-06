# Git TTS

A fun text-to-speech integration for Git that reads your commit messages aloud. This project provides both an interactive TTS terminal interface (bonus) and a Git post-commit hook that automatically speaks your commit messages.

## Features

- **Interactive TTS Interface**: Terminal-based application for converting text to speech
- **Git Integration**: Post-commit hook that automatically reads commit messages aloud

## Demo

<audio controls>
  <source src="https://raw.githubusercontent.com/TALLEC-Scott/git-tts/main/output.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>

## Available Voices

- `expr-voice-2-m` / `expr-voice-2-f` (default male voice)
- `expr-voice-3-m` / `expr-voice-3-f`
- `expr-voice-4-m` / `expr-voice-4-f`
- `expr-voice-5-m` / `expr-voice-5-f`

### Git Hook

The `post-commit` hook automatically generates TTS for your commit messages. To set up:

```bash
cp post-commit .git/hooks/
chmod +x .git/hooks/post-commit
```

After installation, every commit will trigger an async TTS generation of your commit message.

## Requirements for hook 

 All you need is uv [uv](https://docs.astral.sh/uv/), allows for quick installs and
 nice shebangs.

## Credits

This project is built using [KittenTTS](https://github.com/KittenML/KittenTTS), an decent super light text-to-speech model. Special thanks to KittenML.
