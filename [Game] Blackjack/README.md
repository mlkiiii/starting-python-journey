# 🃏 Blackjack – Python Console Game

A console-based implementation of the classic **Blackjack** card game built in Python.

This project is part of my **Starting Python Journey** repository, where I document my growth from beginner to advanced Python developer and future Cybersecurity Engineer.

---

## 🎯 Project Overview

This program simulates a simplified version of Blackjack where:

- The player starts with $5000
- The player places bets each round
- Cards are dealt randomly
- The player can **Hit** or **Stand**
- The dealer follows standard Blackjack rules (hits until 17+)
- The game ends when the player runs out of money or chooses to quit

The game runs entirely in the terminal.

---

## 🧠 Features

- Betting system
- Random card generation
- Dealer logic (hits until 17)
- Blackjack detection
- Bust detection
- Win / Lose / Tie handling
- Persistent round flow until player exits
- Card storage using file handling (`pickle` module)

---

## 🛠️ Technologies Used

- Python 3
- `random` module
- `pickle` module (for storing dealt cards)
- Dictionaries
- Lists
- Loops and conditional logic
- File handling

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:blackjack.py
The game will start in the terminal.

---

## 🎮 Gameplay Flow

1. Player starts with $5000.
2. Player enters a bet amount.
3. Cards are dealt to both player and dealer.
4. Player chooses:
   - `H` or `Hit`
   - `S` or `Stand`
5. Dealer draws cards until reaching 17.
6. Winner is determined.
7. Money updates.
8. Game continues until:
   - Player quits
   - Player runs out of money

---

## 📚 Concepts Practiced

- Game loop structure
- State management (money & bets)
- File handling with pickle
- Card representation using dictionaries
- Conditional game logic
- Input validation
- Modular functions

---

## 📈 What I Learned

- How to simulate real-world game logic
- How to structure a multi-function Python program
- How betting systems affect game flow
- Managing dynamic data (cards and hands)
- Handling user input safely

---

## 🔮 Future Improvements

- Fix Ace value logic (11 or 1 depending on hand)
- Improve card generation accuracy
- Remove file dependency and handle cards in memory
- Implement a proper shuffled deck system
- Add split and double-down options
- Improve UI formatting
- Add OOP structure (Player, Dealer, Deck classes)
- Add probability tracking

---

## 🚀 Project Context

This project is part of my public learning journey:
**Starting Python Journey** – building structured projects from beginner to advanced level.

Each new project improves:
- Code organization
- Logical thinking
- Software design
- Problem-solving ability

---

## 👨‍💻 Author

Malki Mohamed  
Python Developer in Progress | Future Cybersecurity Engineer 🔐  

---

⭐ If you found this project interesting, feel free to star the repository and follow the journey!