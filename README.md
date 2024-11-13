# Game Hub Project

Welcome to **Game Hub** – a collection of classic games written in Python! This hub features Hangman, Tic-Tac-Toe, and Snake Game, all accessible through a single HTML-based interface.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Game Descriptions](#game-descriptions)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [License](#license)

---

## Project Overview
Game Hub serves as a single platform where users can play various popular games directly in a Python environment. This project leverages HTML for a simple frontend interface, with individual games coded in Python.

## Features
- **Classic Games**: Includes Hangman, Tic-Tac-Toe, and Snake Game.
- **Interactive Interface**: Navigate games via a HTML menu.
- **Scorekeeping and Win Detection**: Real-time score updates and game results.

## Requirements
- Python 3.x
- **Turtle Graphics Library**: Used in the Snake game (pre-installed in standard Python distributions).
- **Tkinter Library**: Used for the Tic-Tac-Toe GUI (pre-installed in standard Python distributions).

## Game Descriptions

### 1. Hangman
A terminal-based word-guessing game where the player guesses letters to reveal a hidden word. Be careful – you only get five incorrect guesses before you lose!  
**File**: `hangman.py`  
**Gameplay**: [Sample]  
- Input a letter each round.
- If correct, the letter reveals in the word; if incorrect, a part of the hangman appears.
  
### 2. Tic-Tac-Toe
A GUI-based two-player game built with Tkinter. Players alternate turns to place their mark (X or O) and aim to complete a row, column, or diagonal with their symbol.  
**File**: `tic_tac_toe.py`  
**Gameplay**: [Sample]  
- Interactive buttons allow players to place their marks.
- Displays the result when a player wins or if the game is a draw.

### 3. Snake Game
A classic arcade-style game developed using Turtle Graphics. Control the snake to eat fruits and grow, but avoid hitting the walls or itself.  
**File**: `snake_game.py`  
**Gameplay**: [Sample]  
- Arrow keys control snake direction.
- The score increases with each fruit eaten.

### 3. Fruit Ninja
The game is still in progress, may not work in some computers
**File**: `fruit_ninja.py` 

### Start the gamehub by opening the index.html, this redirects you to main.py which uses a login method to access all the games
