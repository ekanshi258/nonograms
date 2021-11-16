# nonograms

I got bored, so I tried generating nonograms. If I get bored again, I'll build a solver maybe.

## Generate
Run `generate.py` with the required `--rows` and `--cols` options to generate a random nonograms of specified size.

#### Options
- `--rows`: Number of rows on the board (Required)
- `--cols`: Number of columns on the board (Required)
- `--inst`: Show instructions on how to solve the nonogram
- `--seed`: Use this option if you want to use a specific seed for the `random` functions

### Playing
At the moment, it's not interactive. Once you run `generate.py`, it shows you the board on the command line along with the numbers on the rows and columns depicting the number of cells to be coloured. You're gonna have to solve it on paper by yourself.

After you're done, you'll see a prompt asking you if you want to look at a possible solution. Press `Y` or any key to see the solution, or `n` to exit the game.

## Instructions
Numbers on the rows and columns show how many **consecutive** cells should be coloured in that row/column.  
```
. . [1]
. . [0]
1 0
```
Then the solution is:  
```
x . [1]
. . [0]
1 0
```
When there are multiple numbers in the row/column, such as:  

`. . . . . [1, 2]`  


Then there should be a gap of *at least* 1 cell between the two groups of (i.e. consecutive) coloured cells (here, 1 coloured cell and then 2 consecutive coloured cells), like:  

`x . x x . [1, 2]`    (or)   ` x . . x x [1, 2]`    (or)    `. x . x x [1, 2]`  

- `x` -> denotes that the cell is coloured  
- `.` -> denotes that the cell is empty  

## Next
Since there can be many solutions, the given solution may not match with yours. I'll add a checker for solutions, so you can enter your solution on the command line and have it checked.
