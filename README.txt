Vit Pavlik
xpavli0a
251301
May 2024
IAM - solving sudoku with propositional logic and SAT solver

Included files
--------------
.. input.txt
   the assigned input

.. input_2.txt
   different, custom input to demonstrate the functionality

.. minisat-output-translated.txt
   minisat output with the variables in the desired encoding

.. minisat-output.txt
   original minisat output with the variables in my custom, packed encoding
   (729 variables)

.. run.sh
   a script to run everything (use ./run.sh run or ./run.sh clean)

.. sudoku-dimacs.txt
   DIMACS formula generated by sudoku.py

.. sudoku.py
   the main program to generate the formula

.. translate.py
   program to translate variables in minisat output (where the positions are
   encoded by my custom encoding) to the desired encoding

.. view.py
   program to view the minisat output on a sudoku board
   also check validity of the solution


Usage
-----

.. python3 sudoku.py < input-file > dimacs-file
   generate DIMACS file

.. minisat dimacs-file output-file
   run the SAT solver

.. python3 translate.py < output-file > translated-output-file
   translate to desired encoding

.. python3 view.py < output-file
   view model on a sudoku board and check validity of the solution

.. ./run.sh run
   do all of the above (you will be prompted to confirm overwriting files, run
   ./run.sh run -y to skip)

.. ./run.sh clean
   get rid of the generated files (you will be prompted to confirm each file,
   use ./run.sh clean -y to skip)


Prerequisites
-------------

Python scripts were developed using python 3.12.3. Note that there may be
some features used from the typing module that won't work with older python
versions.

Also, I used Debian package minisat 1:2.2.1-5+b3 (bookworm).
