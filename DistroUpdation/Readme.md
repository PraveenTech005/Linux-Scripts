# 🚀 Automatic Distro Update

This Python script automatically updates and upgrades your Linux distribution every 7 days. Say goodbye to manual updates and let automation take care of it! 

### 🤔 Why?
Manually running:
```bash
sudo apt update
sudo apt upgrade
```

  It is a hassle, right? If you're like me and often forget (or you're just lazy 😅), this script will help you keep your system up-to-date effortlessly!

# 📋 Features
- Automates the process of running apt update and apt upgrade on a weekly basis.
- Keeps track of the last update date.
- Displays system info with neofetch after every update.
- Works right from your .zshrc, so your updates happen every time you open a terminal session.

# 🛠 How It Works
- It checks if a file named lastupdated.txt exists. If not, it creates one.
- The script compares today's date with the last update date and ensures updates happen every 7 days.
- If it's time, the script runs sudo apt update && sudo apt upgrade.
- Lastly, it clears the terminal and runs neofetch to display your distro details.

# ⚙️ Setup
- Clone the repo:

```bash
git clone https://github.com/<your-username>/<repo-name>
cd <repo-name>
```
- Place the script in your desired directory (e.g., ~/Scripts).
- Add the following lines to your .zshrc to execute the script every time a terminal session starts:

```bash
sudo nano .zshrc
```
paste the below commands on bottom of all other scripts

  ```.zshrc
cwd=$(pwd)
cd ~/Scripts/
python3 ~/Scripts/auu.py
cd "$cwd"
```
- Enjoy automatic updates!

# 📜 License
    This project is licensed under the MIT License. Feel free to fork, modify, and use it in your own projects!

# Author 
- It's Absolutely Me [PraveenTech005](https://github.com/PraveenTech005)
  
Feel free to contribute or drop any suggestions! 😊

    This includes the program code, instructions on how to add it to `.zshrc`, and all other sections. You can now copy this as your full `README.md`.
