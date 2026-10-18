# simon-game

A "simon" game in pygame. Four colored buttons that
flash a growing sequence for the player to repeat. Built live on stream as a
response to an r/learnpython help request.

Stream: [![/r/learnpython : making a simon game](https://img.youtube.com/vi/dYVi4Y1UNvU/0.jpg)](https://www.youtube.com/watch?v=dYVi4Y1UNvU)

based on a reddit question here: https://www.reddit.com/r/learnpython/comments/qunumo/making_a_genius/ 

## How it works

All in `main.py` (2 classes, \~120 lines):

- **`Button`** — a colored rectangle with a label; `draw(win)` renders it,
  `isOver(pos)` hit-tests the mouse position.
- **`Game`** — holds the `sequence` (list of button indexes), `next_step`
  (player's progress through it), `level` (sequence length, starts at 3), and
  the four buttons. The labels/colors are in Portuguese — `azul` (blue),
  `amarela` (yellow), `verde` (green), `ciano` (cyan) — a nod to the original
  redditor's question ("genius" is the Brazilian name for the Simon game).
- `new_sequence()` picks `level` random buttons and plays the "demo" — the
  current implementation of `play_demo()` just \*\*prints the sequence to the
  console\*\* (flashing the buttons was left as the next step).
- `press_button(i)` — correct press advances `next_step`; completing the
  sequence prints "Você ganhou!" ("you won!"), bumps `level`, and generates a
  longer sequence. A wrong press prints "Errado!", replays the demo, and resets
  progress.
- `main()` — pygame setup: 500×500 window titled "Genius", main loop redraws
  the buttons and routes `MOUSEBUTTONDOWN` clicks to `press_button`.

The git history shows the stream's arc: initial code from the reddit thread →
refactor → extract the `Game` class → input-pattern checking.

## Build / run

```sh
pip install pygame
python main.py
```

Click the buttons in the order printed to the console; the sequence grows by
one each round.
