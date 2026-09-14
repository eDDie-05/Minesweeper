#  Minesweeper Game — Python

##  Overview

**Minesweeper** is a Python-based puzzle game where the player must uncover cells on a grid while avoiding hidden mines. Numbers displayed on revealed cells indicate how many mines are located in the surrounding cells.

The goal is to **clear the entire board without clicking on a mine**.

This project was developed for educational purposes to practice Python programming and game development concepts.

##  Features

*  Randomly placed mines
*  Number indicators showing nearby mines
*  Mouse-based gameplay
*  Flag cells suspected of containing mines
*  Win detection
*  Game-over detection
*  Restart/new game option
*  Graphical user interface

##  Technologies Used

* **Python 3**
* **Pygame** *(if used in the project)*
* 2D lists
* Functions
* Conditional statements
* Event handling
* Random number generation

##  Requirements

Before running the game, make sure you have:

* Python 3.x
* Pip
* Pygame

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/minesweeper-python.git
```

### 2. Open the project directory

```bash
cd minesweeper-python
```

### 3. Install Pygame

```bash
python3 -m pip install pygame
```

### 4. Run the game

```bash
python3 main.py
```

##  Controls

| Action            | Control            |
| ----------------- | ------------------ |
| Reveal cell       | Left Mouse Button  |
| Place/Remove flag | Right Mouse Button |
| Restart game      | `R`                |
| Exit game         | `ESC`              |

> Controls may vary depending on the implementation.

##  How the Game Works

The game creates a grid containing hidden mines.

When a player reveals a safe cell, the game displays a number indicating the number of mines in the surrounding cells.

For example:

```text
┌───┬───┬───┐
│ 1 │ 1 │ 0 │
├───┼───┼───┤
│ 1 │ 💣 │ 1 │
├───┼───┼───┤
│ 1 │ 1 │ 1 │
└───┴───┴───┘
```

The player uses these numbers to determine where mines are located.

### Winning

The player wins when all safe cells have been successfully revealed.

### Losing

The game ends when the player reveals a cell containing a mine.

##  Project Structure

```text
minesweeper-python/
│
├── main.py
├── assets/
│   └── ...
├── requirements.txt
└── README.md
```

##  Project Objectives

This project demonstrates:

* Python programming fundamentals
* 2D arrays/lists
* Random number generation
* Mouse and keyboard event handling
* Game-state management
* Conditional logic
* Grid-based game development
* Graphical user interfaces

##  Future Improvements

Possible improvements include:

*  High-score system
*  Game timer
*  Difficulty levels
*  Sound effects
*  Custom themes
*  Leaderboard
*  Save/load game functionality
*  Game statistics
*  Improved animations

##  Disclaimer

This project is an independent implementation of the Minesweeper puzzle game and is intended for educational purposes.

##  Author

eDDie

Developed using Python as a game development project.

##  License

This project is intended for educational purposes. Check the repository license and included assets before redistributing the project.
