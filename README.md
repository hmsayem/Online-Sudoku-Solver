# Online Sudoku Solver
## About
This Python module can solve even 'hard' sudoku problems almost instantly. It reads any 9x9 Sudoku-puzzle from an online sudoku website [sudoku.game](https://https://sudoku.game/very-hard) and solves the sudoku automatically by interacting with the webpage.

### Rules of Sudoku
You must fill the boxes of a 9x9 grid with numbers from 1 to 9 in a way that there are no recurring numbers in each row, column, and 3x3 block.
### How it works ?

It works with backtracking algorithm.Backtracking is simply reverting back to the previous step or solution as soon as we determine that our current solution cannot be continued into a complete one.
#### Algorithm

Starting with an incomplete board:

1. Find some empty space
2. Attempt to place the digits 1-9 in that space.
3. Check if that digit is valid in the current spot based on the current board.
4. a) If the digit is valid, recursively attempt to fill the board using steps 1-3. <br>
   b) If it is not valid, reset the square you just filled and go back to the previous step. 
5. Once the board is full by the definition of this algorithm we have found a solution.
* Example: <br> <br>
![alt tag](https://raw.githubusercontent.com/kirilkirkov/Sudoku-Solver/master/backtracking_mech.gif)

### From solution to automation
The automation part is divided into two sections: <br>
* Locating the numbers on a sudoku grid. This way we can solve any sudoku without having to fill the sudoku variable manually.
* Filling the empty cells with numbers. <br>

The automation has been done by using the <code> PyAutoGUI </code> module.

### How to Use
#### Clone project & Install Requirements
> Make sure you have already installed python3 and git.
```
git clone https://github.com/hmsayem/Online-Sudoku-Solver.git && cd Online-Sudoku-Solver
pip install -r requirements.txt
```
#### Solving Puzzle
> Open a random puzzle from [sudoku.game](https://https://sudoku.game/very-hard) and run the the main.py script.
```
python main.py
```
