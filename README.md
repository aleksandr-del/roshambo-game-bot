# Rock-Paper-Scissors Telegram Bot

## About the Project

A simple and interactive Telegram bot built with Python using the asynchronous aiogram framework. Allows users to play the classic "Rock, Paper, Scissors" game with the bot through Telegram chat using convenient custom keyboards and detailed instructions in Russian.

## Features

- Rock-Paper-Scissors game against the bot
- Russian language interface with clear messages and hints
- Custom keyboards for quick action and move selection
- Access restriction by user_id list
- Logging with separation of INFO and ERROR logs
- Clean code separation into modules: configuration, filters, handlers, keyboards, services, and localization

## Requirements

- Python 3.11 or newer
- Dependencies from `requirements.txt` (aiogram, environs, etc.)

## Installation and Setup

1. Register your bot with [@BotFather](https://t.me/botfather) and get the token.

2. Clone the repository:

```bash
git clone https://github.com/aleksandr-del/roshambo-game-bot.git
cd roshambo-game-bot
```

3. Create a `.env` file in the project root with the following content:

```env
BOT_TOKEN="your_bot_token"
USER_IDS=123456789,987654321 # Comma-separated list of user_ids who can use the bot
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run the bot:

```bash
python main.py
```

## How to Use

- Send the `/start` command to begin and view the welcome message.
- Click the "✅ Давай!" (Let's go!) button to start the game, or "Не хочу!" (Don't want to!) to decline.
- Choose one of the moves: Rock 🗿, Scissors ✂️, or Paper 📜.
- The bot will show its move and announce the game result (win, loss, draw).
- The `/help` command shows the game rules.

## Project Structure

```
.
├── config/          # Bot configuration via .env
├── filters/         # Message filters (e.g., by user_id)
├── handlers/        # Command and message handlers
├── keyboards/       # Interactive keyboards with buttons
├── lexicon/         # Russian message and button texts
├── logger/          # Logging settings and filters
├── main.py          # Entry point, bot startup and configuration
├── menu/            # Bot main menu commands
├── requirements.txt # Project dependencies
├── services/        # Game logic and helper functions
├── .env.example     # Example environment variables file
└── .gitignore       # Files and folders ignored by git
```

## Game Rules

The classic Rock-Paper-Scissors rules apply:
- Rock 🗿 beats Scissors ✂️
- Scissors ✂️ beats Paper 📜  
- Paper 📜 beats Rock 🗿
- Same choices result in a draw

## Tech Stack

- **Python 3.11+**
- **aiogram 3.x** - Telegram Bot API framework
- **environs** - Environment variable management
- **Modular architecture** - Clean separation of concerns

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Note

The bot interface is in Russian language, designed for Russian-speaking users. The game messages, buttons, and interactions are all in Russian with appropriate emojis and formatting.
