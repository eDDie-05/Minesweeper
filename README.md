# Minesweeper — Python

A desktop Minesweeper-style puzzle built with Python and Pygame.

## Features
- Random mine placement
- Adjacent-mine number calculation
- Grid-based board
- Revealed-cell and flag state
- Win/loss gameplay state

## Requirements
- Python 3.9 or newer
- Pygame

## Run locally
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install pygame
python minesweeper.py
```

## Project files
- `minesweeper.py` — board generation, mine calculation, rendering and interaction

## Current scope
A local puzzle-game exercise. The board currently uses fixed dimensions and mine count in the source. Automated tests and configurable difficulty are future improvements.
