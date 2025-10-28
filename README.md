# Telegram-chatbot
# 🤖 Telegram AI Chatbot (Aiogram + OpenAI GPT-3.5-Turbo)

This project implements a **Telegram Chatbot** using the **Aiogram framework** integrated with **OpenAI’s GPT-3.5-Turbo API**.  
It allows users to chat with an AI assistant directly through Telegram, supporting commands like `/start`, `/help`, and `/reset`.

Developed by **Aryan Singh Parihar**.

---

## 🧠 Project Overview

The project is divided into **two main parts**:

1. **Frontend** (`echo_bot(frontend).py`) — sets up the Telegram bot interface using Aiogram.  
   - Handles basic commands (`/start`, `/help`)  
   - Responds to user messages (echo functionality)  
   - Serves as the connection point between Telegram and Python backend  

2. **Backend** (`main(BACKEND).py`) — integrates OpenAI API with Telegram bot.  
   - Connects GPT-3.5-Turbo to generate intelligent responses  
   - Maintains conversation context  
   - Supports conversation reset and error handling  

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Aiogram** — for Telegram bot handling  
- **OpenAI API (GPT-3.5-Turbo)** — for intelligent responses  
- **dotenv** — for managing environment variables  
- **logging** — for debugging and monitoring  

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/telegram-ai-chatbot.git
cd telegram-ai-chatbot
