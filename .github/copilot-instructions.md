# AI Agent Instructions for wordle-console

This document provides key information for AI coding agents working with the wordle-console project.

## Project Overview

This is a Python-based console implementation of the Wordle game. The project uses the `rich` library for console UI and follows a modular architecture.

## Core Components

- `wordle_game.py`: Core game logic and state management
- `cli.py`: Console UI and user interaction handling
- `vocab.py`: Vocabulary management (loading word lists)
- `data/`: Contains word lists for valid guesses and possible answers

## Project Setup

The project uses `uv` for Python package management. Key commands:

```bash
uv init  # Initialize environment
uv run python -m wordle_cli  # Run the game
```

## Architecture Patterns

1. **Component Organization**
   - Game logic is separated from UI (`WordleGame` class vs `cli` module)
   - Word lists are loaded once at startup via `vocab.py`

2. **Game State Management**
   - Game state is maintained in `WordleGame` class
   - Each guess is stored with its scoring pattern
   - Score values: 0 (absent), 1 (correct), 2 (present in wrong position)

3. **UI Patterns**
   - Rich library components are used consistently:
     - `Panel` for instructions
     - `Table` for game board
     - `Console` for styled output
   - Color scheme defined in `styles` dictionary in `cli.py`

## Data Files

Word lists in `src/wordle_cli/data/`:
- `wordle-allowed-guesses.txt`: All valid guesses
- `wordle-answers-alphabetical.txt`: Possible answers

## Development Workflows

1. To add new features:
   - Core game logic changes go in `wordle_game.py`
   - UI enhancements belong in `cli.py`
   - New word lists should be added to `data/`

2. Project uses `ruff` for linting with max line length of 128 characters.

## Dependencies

Key dependencies (Python 3.12+ required):
- `rich`: Console UI framework
- `pyfiglet`: ASCII art text
- `textual`: TUI framework (not currently used but available)