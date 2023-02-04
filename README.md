## INTRO

A simple video converter whose development was cut short by the client, so now is in my portfolio.

It works, but is very limited and has a few bugs. The UI was built using Kivy and is not great. With a bit more work it can become a very efficient piece of code.

As it is, it resizes a given video to the following:

```
    resolutions: 1920x1080, 1080x1920, 1080x1080, 1350x1080
    codecs: h264
    formats: mp4
```

These can be changed in `vars.json` to any formats supported by `fmpeg`: https://ffmpeg.org/general.html

## MOTIVATION

A video editor wanted to automate their repetitive job resizing and cropping videos for different social media platforms.

## REQUIREMENTS
`python 3.8`
`homebrew`: https://brew.sh
`ffmpeg` (must be installed system wide):

```shell
brew install ffmpeg
```

## RUNNING

1. Create a virtual environment:

```shell
python3 -m venv .venv && . .venv/bin/activate/
```

2) Install the required packages:
```shell
pip install -r requirements.txt
```

3) Run it:
```shell 
python3 -m manager.py
```