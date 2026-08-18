# 🤖 JARVIS — Personal Desktop Voice Assistant

JARVIS is a Python-based personal desktop voice assistant designed to automate everyday computer tasks using **voice recognition, text-to-speech, web automation, system controls, media playback, notes, email automation, and screenshots**.

The project is built to provide a simple voice-controlled interface for interacting with your computer and performing common tasks hands-free.

## ✨ Features

* 🕐 **Time & Date** — Reports the current time and date.
* 👋 **Automated Greetings** — Greets the user according to the time of day:

  * Good Morning
  * Good Afternoon
  * Good Evening
* 📚 **Wikipedia Integration** — Searches Wikipedia and reads a short two-sentence summary of requested topics.
* 📧 **Email Automation** — Sends emails through Gmail's SMTP server using voice commands.
* 🌐 **Web Navigation** — Opens requested websites using Google Chrome.
* 💻 **System Controls** — Supports:

  * Logout
  * Restart
  * Shutdown
* 🎵 **Media Playback** — Plays music from a specified local music directory.
* 📝 **Memory & Notes** — Saves quick notes to `data.txt` and reads saved notes when requested.
* 📸 **Screenshots** — Captures the screen using `pyautogui`, asks for a filename through voice input, and saves the screenshot locally.
* 🎙️ **Voice Interaction** — Uses speech recognition for receiving commands and text-to-speech for responding.

## 🛠️ Technologies Used

* **Python 3**
* **SpeechRecognition**
* **pyttsx3**
* **Wikipedia**
* **PyAutoGUI**
* **Gmail SMTP**
* **Google Chrome**
* Python standard libraries:

  * `datetime`
  * `smtplib`
  * `webbrowser`
  * `os`

## 📋 Prerequisites

Before running JARVIS, make sure you have:

* Python 3.x installed
* Google Chrome installed
* A Gmail account if you want to use the email functionality
* A local music directory if you want to use music playback

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Install the required Python packages:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyautogui
```

> **Note:** `datetime`, `smtplib`, `webbrowser`, and `os` are built into Python and do not require separate installation.

## ⚙️ Configuration

Before running the application, update the configuration values in the Python script according to your computer.

### 📧 Email Credentials

Configure the email function with your Gmail account.

For Gmail, it is recommended to use a **Google App Password** instead of your regular Gmail password.

Never commit passwords, API keys, or other sensitive credentials to GitHub.

### 🌐 Chrome Path

Update the Chrome executable path in the script if your Chrome installation is located somewhere different from the configured path.

Example:

```python
chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe"
```

### 🎵 Music Directory

Update the music directory to the folder containing your local music files.

Example:

```python
songs_dir = "D:/Music"
```

### 📸 Screenshot Directory

Update the screenshot save location according to your system.

Example:

```python
screenshot_dir = "C:/Users/YourUsername/Desktop/JARVIS"
```

> Replace `YourUsername` with your actual Windows username.

## ▶️ Running JARVIS

Run the Python script from your terminal or command prompt:

```bash
python your_script_name.py
```

After starting, JARVIS will greet you and wait for your voice commands.

## 🎙️ Example Voice Commands

You can interact with JARVIS using commands such as:

```text
"What is the time?"
"Tell me the date."
"Search Wikipedia for Python."
"Send email."
"Search in Chrome."
"Play songs."
"Remember that I have an exam tomorrow."
"Do you know anything?"
"Take a screenshot."
"Shutdown."
"Restart."
"Logout."
"Offline."
```

## 📁 Project Structure

A basic project structure can look like this:

```text
JARVIS/
│
├── jarvis.py
├── data.txt
├── requirements.txt
└── README.md
```

## 🔐 Security Notes

JARVIS interacts with your local computer and may handle sensitive operations such as email and system power controls.

For security:

* Do not hard-code your Gmail password.
* Use Gmail App Passwords where applicable.
* Never upload credentials or secrets to GitHub.
* Add sensitive configuration files to `.gitignore`.
* Review system-control commands before executing them.

## 🚀 Future Improvements

JARVIS can be extended with more advanced capabilities, including:

* 🤖 AI-powered conversational intelligence
* 🧠 Long-term memory
* 🔊 Improved voice recognition
* 🌐 More web automation
* 📱 Mobile application integration
* 🖥️ Advanced desktop automation
* 🔐 Secure authentication
* 🗄️ Database-backed memory
* ⚡ FastAPI backend
* 🔌 Extensible tool/plugin system

## 👨‍💻 Author

**Harsh Dixit**

Built with Python to explore voice assistants, desktop automation, and AI-powered applications.

## ⭐ Contributing

Contributions, improvements, and feature suggestions are welcome.

If you find this project useful, consider giving the repository a ⭐ on GitHub.
