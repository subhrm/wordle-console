# Wordle Console: Hint Feature Specification

## Overview
Add a hint feature to the Wordle console game. At any turn, the user may type "hint" to receive a list of possible words that match the current game state.

## Goals
- Allow user to type "hint" instead of a guess during their turn.
- Display a filtered list of possible answer words based on previous guesses and their feedback.
- Integrate seamlessly with existing game loop and UI.

## Requirements
1. **User Input Handling**
   - Accept "hint" as a valid input during guess prompt.
   - Prevent "hint" from counting as a guess or affecting game state.

2. **Hint Generation Logic**
   - Filter possible answer words using:
     - Letters known to be correct (green)
     - Letters known to be present but misplaced (yellow)
     - Letters known to be absent (gray)
     - Position constraints from previous guesses
   - Use existing word lists from `vocab.py` and `data/`.

3. **UI/Console Output**
   - Display a panel or table of possible words (limit to N, e.g., 10-20 for readability).
   - Style output using `rich` for clarity.
   - Optionally show count of remaining possible words.

4. **Integration Points**
   - Update `cli.py` to handle "hint" input and display results.
   - Add hint logic to `wordle_game.py` (new method or utility).
   - Ensure vocabulary filtering uses loaded word lists.

5. **Testing & Edge Cases**
   - Handle cases with no possible words (contradictory guesses).
   - Ensure hints do not reveal the actual answer directly.
   - Validate performance for large word lists.

## Implementation Steps
1. Update input loop in `cli.py` to accept "hint".
2. Add hint generation method to `WordleGame`.
3. Filter possible words using current game state.
4. Display hint results in console using `rich`.
5. Test with various game scenarios.

## Acceptance Criteria
- User can type "hint" at any turn and receive a list of possible words.
- Hint list updates dynamically based on guesses and feedback.
- No disruption to normal gameplay or scoring.
- Output is clear, readable, and limited in size.
