# Ping bot

![GitHub](https://img.shields.io/github/license/RoLO0u/ping-bot?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/RoLO0u/ping-bot?style=for-the-badge) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/RoLO0u/sticker-bot?style=for-the-badge) ![Python Version](https://img.shields.io/badge/Python-3.12-informational?style=for-the-badge&logo=python) ![GitHub watchers](https://img.shields.io/github/watchers/RoLO0u/ping-bot?style=for-the-badge)

# Installation

Bot simply can be installed by running code on machine using required variables in .env file

## Installation guide step by step

1. Requirements

* [Python >3.10.x](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/installation/)
* [git](https://git-scm.com/downloads)

2. Clone project

```console
git clone https://github.com/RoLO0u/ping-bot.git
```

3. Install python requirements

```console
pip install -r requirements.txt
```

4. Set environment variables

Environment variables can be seen in *Required variables* part or in *.env.example* file

5. Run programm

To run programm use simple command depending on your configuration:

```console
python main.py
```

```console
python3 main.py
```

```console
python3.11 main.py
```

```console
py main.py
```

Or use virtual environment variables AND docker

# Required variables

## Telegram bot configuration

* BOT_TOKEN ─ token bot will use to interact with telegram API
> Use [@BotFather](https://t.me/BotFather) to get bot token

# API

This bot uses aiogram, therefore [official telegram api](https://core.telegram.org/bots/api)

# Resources

* [aiogram 3 documentation](https://docs.aiogram.dev/en/dev-3.x/)

* [Telegram API](https://core.telegram.org/bots/api)

* [Anti-flood bot](https://github.com/RoLO0u/anti-flood-bot)
