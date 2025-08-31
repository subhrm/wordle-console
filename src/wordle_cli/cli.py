from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box
from pyfiglet import Figlet
from .wordle_game import WordleGame

console = Console()
fig = Figlet(font="slant")

game = WordleGame(seed=2002)


class GuessValidator:
    def validate(self, text):
        text = text.lower()
        if not game.validate_guess(text):
            raise ValueError("Please enter a valid 5 letter word.")


def cli():
    console.print(fig.renderText("WORDLE IN CONSOLE"), style="bold green")
    for i in range(6):
        guess = ""
        while True:
            try:
                guess = Prompt.ask(
                    f"[bold blue]Guess {i + 1}[/bold blue]: Enter a 5 letter word",
                    default="",
                    console=console,
                )
                GuessValidator().validate(guess)
                break
            except ValueError as e:
                console.print(f"[bold red]{e}[/bold red]")

        guess = guess.lower()
        if game.check_answer(guess):
            console.print(fig.renderText(guess.upper()), style="bold green")
            console.print(
                Panel(
                    "Congratulations!! You have found the word !",
                    style="bold green",
                    box=box.ROUNDED,
                )
            )
            console.print(fig.renderText("Winner"), style="bold green")
            break

        r = game.find_match(guess)
        out = []
        for c in r[0]:
            if c == "*":
                out.append(Text("*", style="bold red"))
            elif c == "?":
                out.append(Text("?", style="bold yellow on black"))
            else:
                out.append(Text(c, style="bold green"))
        response_text = Text.assemble(*out)
        console.print(
            Panel(
                response_text,
                title="Response",
                style="bold",
                box=box.ROUNDED,
            )
        )

    if not game.is_solved:
        console.print(
            Panel(
                "Sorry, you failed to solve it with 6 guesses!!",
                style="bold red",
                box=box.ROUNDED,
            )
        )
        console.print(
            Panel(
                f"The answer is : {game.secret}",
                style="bold red",
                box=box.ROUNDED,
            )
        )
