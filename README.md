# ChessPlayer
A chess AI 

A. Preliminaries:
==================

For this assignment, we will explore the use of the data structures we've 
learned to write a basis chess solver.

You will use PYTHON 3 for this assignment, on ECF.

The assignment MUST be done as individuals, with NO GROUP WORK.

This assignment is worth 5% of your final grade.

Please read this whole document so you understand the overall goals.
Start early.
Ask questions on Discourse.

First some research and some thinking:
---------------------------------------
* consult wikipedia and become familiar with the rules of the game
  you can ignore:
     * pawns get to move two spaces during their first move
     * en passant
     * castling
* how would you represent the state of the chess board
* how would you compute whether a win has occured
* how would you deal with looking ahead to plan your next move

Next, some prototyping with TicTacToe:
---------------------------------------
A TicTacToe solver can be made via the strategy:
* take the winning move if there is one
* take the nonlosing move if there is one
* generate a set of candidate next steps by enqueuing these
  next steps (i.e., the board states that result when these next
  steps were taken), then evaluate these next steps to see if any
  one is BETTER than the other
  -> take this "BETTER" option
* take a random move if there is no such better option

Q: How would you evaluate these next steps?
A: You would simulate what an opponent would do

Q: How would you simulate?
A: One basic method would be to see whether there are clear winning
or non-losing moves that the opponent should tale

Q: Is that it?
A: No, of course not: you can arbitrarily enhance the complexity of the
solver. But ignore this: start with the above simple mechanism.

Exercise:
* get your esc180 tic tac toe solver functions working
* structure your functions so you can play a game with yourself
  (i.e., no computer in the loop)
* create a function for an automatic player that takes the board
  state as an argument and generates a move
  (make sure it takes an arg for "X" or "O" so you can run this
  player for any case)
* structure your functions so you can play a game against the computer
  with a simple computer opponent who:
     * selects winning move, if available
     * selects non-losing, if available
     * selects random move
* now start to explore the the addition of a new mode, before the
  random move, which does the exploration mentioned above
* how would you improve this with a two step look ahead
* how would you arbitrarily improve this

EXPECTATION:
There is NO due date for this preliminary assignment, however, I expect
that by Mon Jan 28, you will have completed this. That is, I expect that
you begin working on this IMMEDIATELY (Mon Jan 21).

B. EZ-Chess Auto Player
=======================
The goal is to write an EZ-Chess playing function that can serve as
an automatic player.

The final project will be due the MONDAY after your February break
(Feb 25).

Below, I include some description of the chess gameplay and also
provide some preliminary exercises to get you closer to the final
deliverable. It is highly advantageous to perform these exercises
by the end of the week of Feb 1.

B.1. PRELIMINARIES

a. The Playing Board is an 8x8 grid of black and white
   squares, organized as follows:
         row7   #_#_#_#_
         row6   _#_#_#_#
         row5   #_#_#_#_
         row4   _#_#_#_#
         row3   #_#_#_#_
         row2   _#_#_#_#
         row1   #_#_#_#_
         row0   _#_#_#_#
   where _ is a BLACK square, # is a WHITE square

   The far right entry of row0 is a white square. To its left
will be a black square, to its left will be a white square.
Above the far right square of row0 (i.e., the far right square of
row1) is a black square. And so on.
   
   Represent the board via a list of integers:
   [  ..... ,  \   <- the 8 elements of row 0
      ..... ,  \
      .....  ]     <- the 8 elements of row 7

   The white player pieces will occupy rows 0 and 1
   initially (i.e., elements 0 through 15), while the black player
   pieces will occupy rows 7 and 6 initially (i.e., elements 48 to 63).

   Regardless of your thoughts/opinions on the matter, DO NOT CHANGE
   the data structure for the board!

An empty board position has a value of 0. A
board position that is occupied will have a value
given by: Offset+Value

White: Offset=10
Black: Offset=20

Piece: Value
Pawn:   +0
Knight: +1
Bishop: +2
Rook:   +3
Queen:  +4
King:   +5

b. EZ-Chess is a primitive form of chess without the modern
   innovations of (a) castling, (b) pawns that move two spaces,
   and (c) en passant.

The only acceptable moves:
*  Pawns can only move towards the opponent, one step at a time in the
   straight forward direction (forward=> towards the opponent)
   unless blocked by another piece.
*  a Pawn can only capture an opposing piece, via the mechanism:
   Pawn travels diagonally forwards (either left or right) by one step.
*  a Knight can jump over pieces to a square that is either unoccupied
   or occupied by the opponent. If the space is occupied by an opponent,
   then you have captured the opponents piece.
   The move is always 3 spaces, in which there is ONE turn (I.e., a three
   space L-shaped path).
*  a Bishop can travel diagonally, any number of spaces until it is
   blocked. If blocked by your own piece, then you can not go up to or
   past your piece. If blocked by your opponent, you may go any number
   of spaces up to the position of your opponent's piece; if you go
   to your opponent's piece position, you will occupy the opponent's
   space (and capture the piece that was present at that space).
*  a Rook can travel in straight lines, any number of spaces until it
   is blocked. If blocked by your opponent, you may occupy
   the opponent's space (in which case you have captured the piece).
*  a Queen can behave as a Rook or a Bishop
*  a King can travel like a Rook or a Bishop, but only one space at
   a time.

c. The object is to attack the King of your opponent; the
   complement is true: you must prevent your King from being attacked.

d. When a King is under attack, and CAN NOT escape the attack
   i.e., the King can not move out of the attack
         another piece can not capture the attacking piece
         another piece can not go between the attacking piece
         to neutralize the attack
   the game is LOST by the King that was attacked.

e. Specifics:
*. When A places a piece, so that the piece's NEXT move would
   result in capturing the King of B: B's King is under threat. We say
   "B is in Check"
*. B is then forced to neutralize the threat via:
   i. moving the King to a square that is not under attack
   ii. capturing the opposing piece that is attacking the King
   iii. placing another piece of B in the line of attack
        (note: this is NEVER possible if A's attacking piece is a Knight
        since Knight's are the only piece that can jump over pieces)

f. If the opponent can take an action to take the King out of Check
   (i.e., so that the King is not being attacked by an opposing piece)
   then the opponent MUST take that action

B.2. ASSIGNMENTS
=================
These are assignments that you should execute as they move you closer to
completion of the project.

1. Write the function GetPlayerPositions(board,player)
   where board is the list data struct that represents the chess board
   (described above) and player is 10 (for white) and 20 (for black).
   It should return a list of all positions that the player occupies.

2. Write the function GetPieceLegalMoves(board,position)
   which will return a list of all legal positions that the piece in
   the given position can take.

3. Write the function IsPositionUnderThreat(board,position,player)
   which will return True if the position is under threat by the opponent
   of the given player

4. How would you decide on candidate moves? Once you have generated a list
   of candidate moves, how would you analyze which of the candidates leaves you
   in a better state? How can a Tree be useful in this case?

Write as much of the above as you can. If you can't write something, you
should try to understand why not, and attempt to surmount the issue.

C. INTEGRATION
==============
Now that you have:
* a method to print the state of the board
* methods to generate candidate moves
* methods to assess the quality of a move

it is time to integrate these to produce a gameplayer.

Part I:
First, create a two-player chess game where two human players can play chess
against each other. Make sure that you can display the state of the board
in a manner that you can comprehend the state of the board.

Pseudocode of the logic (which you can translate to Python):

   import your helper functions

   initialize the state of the board to be the board with White and Black
   arranged properly

   done=False
   while not(done):
      print the state of the board
      ask player White for a move
      verify this is a legal move otherwise re-ask for a move

      print the state of the board
      ask player Black for a move
      verify this is a legal move otherwise re-ask for a move

Play Chess against yourself with this program and verify it
basically works. Note: there is no intelligence apart from
the check that the move is legal.

If you're confused as to how to "ask player for a move", note that
a move is defined by the player entering two numbers: the first number
is the location in the 1-D board array that corresponds to the piece
the player wants to move, and the second number corresponds to where
the player wants to move it.

Part II:
Now start to incorporate some testing of your functions that you did in Part B
(due a few weeks ago, if you followed my recommendations).
Modify the code above (saving it to a separate filename first), so that
instead of asking for a move you:
   * GetPlayerPositions and print the positions
     (so you can verify this works)
   * for each of the above positions, call GetPieceLegalMoves and
     print the legal moves (so you can verify this works)
   * for each of the legal moves, call IsPositionUnderThreat, so you 
     can measure where the move will result in your piece being captured

Do you see how these simple functions can be exploited to write an automatic
player?

If not, then try this:
Write a function that has this logic (the below omits details but provides
major clues as to the logic; you will have to adjust this code as needed):
    accum = []
    L = GetPlayerPositions
    for moves in L:
       for i in moves:
          if not(IsPositionUnderThreat(i))
              accum = accum + [i]
    

What does this do? It creates a list, accum, that will contain the
moves for which the player is not at risk of capture.

Now use this function, instead of asking player White (or Black; choose one)
for a move.

At first, pick a random move out of the accum.

Part III:
Above we introduced a simple measure for an automatic player: pick, randomly, a
move that does not result in my piece being consumed by the opponent.

But is this really apt in Chess?

Alternate strategies may involve you:
* trying to get control of a section of the board
* opening up paths for your important pieces (usually queen > rook > bishop)
* bringing the knights out so they control their maximal span of locations
* attacking high value pieces of your opponent (where "high value" depends on your
  strategy, but you may consider pawn < knight/bishop < rook < queen < king)

etc.

You may decide to prioritize these strategies. You may decide to employ secondary
strategies after primary ones: and you may exploit the tree (general trees) to manage
the complexity. You may then decide to traverse the tree and assign scores to each 
candidate move, and then pick the best move. Or perhaps you employ a random selector.
Or maybe both.


Grading:
This part_3 is still an ungraded assignment, but like parts 1 and 2 will result in you
writing code that will be used for the final submission.

If you've written the above you're very close apart from some interface tweaks so that our functions
can interoperate.

How you print the board is immaterial to me. What I want ultimately from your chess player
is a move. So your print function is purely for your own benefit to debug the work: hence you
can make it as complex/simple as needed for your own benefit.

D. DELIVERABLE
==============
Due: 11:59PM on 25 Feb 2019; no extensions will be granted

Assignment 1: Chess Player Submission Specifications

A. chessPlayer.py
This file (chessPlayer.py) must contain all of your helper functions and code
for your chess player. It can not contain any code that is not:
* an import statement
* a function definition

It can contain any number of imports and function definitions, but must include
a function called chessPlayer defined as:

* name: chessPlayer
* return values: the 4-list [ status, move, candidateMoves, evalTree]
* arguments: board, player

where: status = True when the function succeeded
                False when the function can not compute a move
                      due to some error condition

       move is a 2-list that consists of two numbers between 0 and 63
        move[0] is the location of the piece chessPlayer intends to move
        move[1] is the location on the board that chessPlayer indents to
                move the aforementioned piece (at move[0]) to

       candidateMoves is a list of 2-lists where:
         candidateMoves[i][0] is a 2-list corresponding to a move
         candidateMoves[i][1] is some floating point number that is a measure
                           of how good or bad the move
                           candidateMoves[i][0] is
         candidateMoves MUST include "move"
         e.g., [ [[1, 5], 0.5],
                 [[10, 25], 0.25],
                 [[63, 0], 0.75] ]
         is a list of three candidate moves.

       evalTree can be:
           * None if you did not use a tree to evaluate potential cases
           * a tree if you did use a tree to evaluate potential cases.
             If you used a tree, return that tree via this return value.
             Specifically, return a LIST that is the level order traversal
             of your tree.
    Reference from your labs:
    def Get_LevelOrder(self):
        x=queue()
        x.enqueue(self.store)
        accum=[]
        while True:
            y=x.dequeue()
            # y is a 2-list where y[0]=True/False
            # and y[1] is the actual dequeued value when y[0]=True
            if (y[0]==False):
                break
            else:
                v=y[1]
                accum=accum+[v[0]]
                for i in v[1]:
                    x.enqueue(i.store)
        return accum

       board is the data structure mentioned in the asssignment Specifications
             (a 64-list of integers, as specified)
             YOUR FUNCTION MUST NOT CHANGE board

       player is 10 for White and 20 for Black, as specified

       A location in the board is either 0 (unoccupied) or has
       one of the following values:
       Piece:   Value
       Pawn:   offset+0
       Knight: offset+1
       Bishop: offset+2
       Rook:   offset+3
       Queen:  offset+4
       King:   offset+5
       where offset is either 10 (White), or 20 (Black).

When the submission window opens, you will
submit this file using the same submit command you use for labs,
with 0 being the arg.
If you wish to submit more than one .py file, they must be named:
chessPlayer_<SUFFIX>.py, where <SUFFIX> is whatever legal string you choose.
E.g., if you write a helper tree data structure class, it should be contained
in a file called chessPlayer_tree.py, not tree.py.

B. Grading
1.5 points (of 5):
   You have written a chess player that produces several candidate moves
   which are ALL legal, and for which you have produced valid scores
   (scores must be floats; you compute them as per your strategy).
   "Several" means: you produce at least as many candidate moves as there
   are legal moves for your player.

1 points (of 5):
   If more than 50% of calls to your function produce an evalTree (as opposed
   to None).

1 point (of 5):
   This is based on your relative score against a chess player that I will
   write. "Relative score" means how well you perform against my chess player
   relative to your classmates.

1.5 points (of 5):
   This is based on your relative score against the top several chess playing
   programs in the class (as identified in the tests against my player).

Note:
The chess player WILL NOT be played to the end (i.e., to a checkmate).
I will run it for some number of moves and compute a score based on
the pieces the player was able to capture and the player's captured
pieces.

If your program uses so much memory that it crashes: that will result in a
game player score of 0.

I will enforce a timeout of 10 seconds per move.
