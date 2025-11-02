from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box
from pyfiglet import Figlet
from .wordle_game import WordleGame

console = Console()
fig = Figlet(font="slant")

game = WordleGame()

styles = {
    "correct": "bold white on green",
    "present": "yellow on blue",
    "absent": "bold black on white",
}


def draw_table() -> Table:
    table = Table(box=box.ROUNDED, style="bold cyan", show_lines=True)
    table.add_column("Guess #", justify="center", style="bold magenta")
    for i in range(1, 6):
        table.add_column(f"Letter {i}", justify="center", style="bold")

    i = 0
    for guess, score in game.guesses:
        i += 1
        row = [str(i)]
        for idx, (char, s) in enumerate(zip(guess, score)):
            if s == 0:
                cell = Text(char.upper(), style=styles["absent"])
            elif s == 2:
                cell = Text(char.upper(), style=styles["present"])
            else:
                cell = Text(char.upper(), style=styles["correct"])
            row.append(cell)
        table.add_row(*row)

    return table


def cli():
    console.print(fig.renderText("WORDLE IN CONSOLE"), style="bold yellow")
    console.print(
        "Welcome to Wordle in Console! Try to guess the 5-letter word.",
        style="bold green",
    )

    inst = Panel(
        title="[blue]Instructions",
        renderable=Text.from_markup(
            f"""[bold cyan]Instructions:[/bold cyan]
- You have 6 attempts to guess the secret 5-letter word.
- After each guess, you'll receive feedback:
    - [{styles["correct"]}] Correct [/{styles["correct"]}]: Correct letter in the correct position.
    - [{styles["present"]}] Present [/{styles["present"]}]: Correct letter in the wrong position.
    - [{styles["absent"]}] Absent [/{styles["absent"]}]: Letter not in the word.
- Use this feedback to refine your guesses and find the secret word!
- Good luck and have fun!"""
        ),
        style="bold",
        width=80,
    )
    console.print(inst)

    while True:
        i = len(game.guesses)
        console.print(f"You have {6 - i} guesses left.", style="bold blue")
        guess = Prompt.ask("Enter your 5-letter guess (or type 'hint'): ").strip().lower()
        if guess == "hint":
            if hasattr(game, "get_hints"):
                possible_words = game.get_hints()
                if possible_words:
                    max_display = 15
                    shown = possible_words[:max_display]
                    table = Table(title=f"Possible words ({len(possible_words)})", box=box.SIMPLE)
                    table.add_column("Word", style="bold yellow")
                    for w in shown:
                        table.add_row(w.upper())
                    if len(possible_words) > max_display:
                        table.add_row(f"...and {len(possible_words) - max_display} more")
                    console.print(table)
                else:
                    console.print("No possible words found. Check your previous guesses.", style="bold red")
            else:
                console.print("Hint feature not implemented.", style="bold red")
            continue
        if len(guess) != 5 or not guess.isalpha():
            console.print("Please enter a valid 5-letter word.", style="bold red")
            continue

        result = game.play(guess)
        if not result:
            console.print(f"'{guess}' is not in the word list. Try again.", style="bold red")
            continue

        console.print(draw_table())

        if game.is_solved or len(game.guesses) == 6:
            break

    if game.is_solved:
        console.print(fig.renderText("WINNER"), style="bold green")
        console.print(
            f"Congratulations! You've guessed the word '{game.secret.upper()}' correctly!",
            style="bold green",
        )
    else:
        console.print(
            f"Game Over! The correct word was '{game.secret.upper()}'. Better luck next time!",
            style="bold red",
        )
