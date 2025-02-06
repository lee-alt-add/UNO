Below is a README for the provided code. This document explains the purpose of the code, its structure, and how to use it.

---

# UNO Game Implementation in Python

## Overview

This Python script simulates a simplified version of the card game UNO. It includes functionality for both a user (player) and a computer-controlled opponent (CPU). The game supports basic UNO rules, including number cards, action cards (e.g., "Draw Two," "Skip," "Reverse"), and special cards like "Wild" and "Wild Draw 4."

## Features

- **Card Dealing:** Randomly assigns cards to players.
- **Turn-Based Gameplay:** Alternates turns between the user and CPU.
- **Action Cards:** Implements "Draw Two," "Skip," "Reverse," "Wild," and "Wild Draw 4" functionalities.
- **Deck Management:** Ensures cards are drawn from the deck when necessary and removes played cards from the deck.
- **Top Card Display:** Shows the current top card on the discard pile.
- **User Interaction:** Allows the user to choose which card to play or draw from the deck.

## Code Structure

The code is organized into a class named `cards`, which contains methods for various game functionalities:

1. **`dealer`:** Determines who will be the dealer by comparing randomly drawn cards.
2. **`hand`:** Distributes cards to the player.
3. **`top_card`:** Selects a valid starting card for the discard pile.
4. **`top_card_view`:** Displays the current top card on the discard pile.
5. **`view`:** Lists the user's available cards.
6. **`PLAY_user`:** Handles the user's turn, including playing or drawing cards.
7. **`PLAY_cpu`:** Handles the CPU's turn, including playing or drawing cards.

## How to Use

### Prerequisites

- Python 3.x installed on your system.

### Instructions

1. Save the code to a file named `uno_game.py`.
2. Run the script using the command:
   ```bash
   python uno_game.py
   ```
3. Follow the on-screen prompts to play the game:
   - Choose actions such as dealing cards or drawing cards.
   - Select which card to play based on the available options.
   - Declare colors when playing "Wild" or "Wild Draw 4" cards.

### Example Gameplay

1. **Determine Dealer:**
   - Both the user and CPU draw a card. The player with the higher number becomes the dealer.

2. **Gameplay Loop:**
   - On each turn, the user can either:
     - Play a valid card from their hand.
     - Draw a card if no valid move is available.
   - The CPU follows similar rules during its turn.

3. **End of Game:**
   - The game continues until one player runs out of cards. At this point, the player with no cards left is declared the winner.

## Notes

- The script assumes that the user is familiar with basic UNO rules.
- Some edge cases may not be fully handled, so additional testing and refinement may be required for a production-level implementation.
- The game does not include scoring or multiple rounds but can be extended to support these features.

## Customization

You can modify the following aspects of the game:

- **Card Deck:** Adjust the `numbers`, `colors`, and `others` lists to include or exclude specific cards.
- **Rules:** Modify the logic in the `PLAY_user` and `PLAY_cpu` methods to implement custom rules or behaviors.

---

Feel free to share this README with others or integrate it into your project documentation!
