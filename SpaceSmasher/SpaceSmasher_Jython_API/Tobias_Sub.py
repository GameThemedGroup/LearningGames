from SS_API import *


@initializeBlockSet
def init_block_set(spaceMaker):
    numRows = 5
    numCols = numRows
    initializeRowSize(numCols)
    count = 0
    for y in range(0, numRows):
        for x in range(0, y):
            addIceBlock()
            count += 1
        for x in range(0, numRows-y):
            addFireBlock()
            count += 1
    revealAllPowers()

startProgram()
