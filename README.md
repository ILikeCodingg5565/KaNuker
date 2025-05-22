# 🎯 KaNuker

> **A Free Educational Tool**

btw this README.md was written by ChatGPT (4o)

KaNuker is a **powerful Python-based Kahoot bot spammer** made for educational and experimental purposes only. Launch waves of bots into any game with custom settings, and watch the lobby light up.

---

## Table of Contents

[AV flags](https://github.com/ILikeCodingg5565/KaNuker/edit/main/README.md#%EF%B8%8F-windows-protected-your-pc-warning)  
[Is it malicious](https://github.com/ILikeCodingg5565/KaNuker/blob/main/README.md#%EF%B8%8F-but-is-it-actually-malicious)   
[Features](https://github.com/ILikeCodingg5565/KaNuker/blob/main/README.md#%EF%B8%8F-features)   
[Installation](https://github.com/ILikeCodingg5565/KaNuker/blob/main/README.md#-installation--usage)   
[Contributions](https://github.com/ILikeCodingg5565/KaNuker/blob/main/README.md#-contributing)   
[Roadmap](https://github.com/ILikeCodingg5565/KaNuker/blob/main/README.md#-roadmap--future-plans)   
[Credits](https://github.com/ILikeCodingg5565/KaNuker/blob/main/README.md#-credits)   

### 🛡️ "Windows protected your PC" Warning

When launching the EXE, Windows may show a **"Windows protected your PC"** message. This happens because the file isn’t from a verified publisher.
#### Verifying the EXE would cost up to $300 USD a year.

To run it anyway:
1. Click **"More info"**
2. Click **"Run anyway"**

> 💡 This is normal for unsigned EXE files. The program is safe — you can inspect the source code or decompile the EXE to verify.

### 🧪 Antivirus & VirusTotal Flags

You might notice the EXE gets flagged by **Windows Defender** or shows warnings on **VirusTotal**. Here's why:

#### ❓ Why is this happening?

- **The EXE is generated from Python using tools like PyInstaller**, which package your script and Python interpreter into one file. This technique is sometimes abused by malware authors — so antivirus engines often flag **any** such EXEs as "suspicious."
- **The file is unsigned**, meaning there’s no digital signature proving it came from a trusted source.
- **Low reputation**: Since this is a new and custom-built tool, it hasn’t been downloaded or whitelisted much, so automated systems assume it's risky by default.

#### 🛠️ But is it actually malicious?

**No. The source code is included** in the repo (`main.py`) — feel free to:
- Read it
- Run it directly in Python
- Compile it yourself using tools like `pyinstaller`

If you’re still unsure, **you can upload your own compiled version to VirusTotal** to compare with mine.

> 💡 False positives are very common with small Python tools packaged into EXEs. If in doubt, run the `.py` directly!



## ⚙️ Features

KaNuker v1 keeps it simple and effective:
- 🔢 Enter a Kahoot Game PIN  
- 🧠 Choose a base name (each bot gets a unique random suffix)  
- 🤖 Pick how many bots to send  
- ⏱ Set a cooldown delay between each join  

---

## 📦 Installation & Usage

### 🔁 Quick Start (Windows Users)

Grab the latest **EXE release** [here](https://github.com/ILikeCodingg5565/KaNuker/releases) and run it—no Python knowledge needed.

### 🐍 Python Enthusiasts

Prefer running the source?

1. Clone the repo or download `main.py`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python main.py
   ```

> 💡 You can also use any online Python interpreter **(with support for `kahoot` imports)** if you’d rather not run this locally.

---

## 🔒 Safety

This project is clean and open.  
**No malware, no surprises.**  
Feel free to inspect the source or decompile the EXE if you want peace of mind.

---

## 🤝 Contributing

Got ideas? Found bugs?  
- ✨ Open an issue with your suggestions  
- 🔀 Fork the repo to add new features  
- 📬 Pull requests welcome!

Collaboration is encouraged—let’s make it better together!

---

## 🛣 Roadmap & Future Plans

Here’s what’s cooking:

### ✅ Smarter Name Generation  
Less obvious bot names = better trolling.
Currently bot names are `name_xxxx` where 'xxxx' is a 4 digit number.

### 🚀 Faster Bot Launching  
Current performance is decent but could be quicker. Optimization on the way!

### 📡 More Advanced Control Panel (v2?)  
GUI or TUI options for easier use? Maybe!

---

## 🙌 Credits

Massive thanks to [@vehbiu](https://github.com/vehbiu) 💖  
Your `kahoot` Python package made this all possible.

---

> ⚠️ **Disclaimer**: This project is for educational purposes only. Please use responsibly and ethically.


## Update Logs
Added V1
