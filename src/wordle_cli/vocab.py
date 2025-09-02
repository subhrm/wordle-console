from pathlib import Path

def load_vocab() -> tuple[set, set]:
    module_path = Path(__file__)
    data_dir = module_path.parent / "data"
    guesses_file = data_dir / "wordle-allowed-guesses.txt"
    possible_answers_file = data_dir / "wordle-answers-alphabetical.txt"

    try:

        with open(guesses_file) as fin:
            possible_guesses = set(fin.read().split("\n"))

        with open(possible_answers_file) as fin:
            possible_answers = set(fin.read().split("\n"))

    
    except Exception as e:
        print(f"{data_dir=}")
        print(f"Error in loading vocab files {e}")
        raise e
    
    return possible_answers, possible_guesses