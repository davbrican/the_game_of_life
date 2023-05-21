import cell
import board
import random
import os
import time

def main():
    iteration = 0
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    board1 = board.board(width, height)
    for i in range(width):
        for j in range(height):
            board1.add_cell(cell.cell(i, j, random.choice([True, False])))
            #board1.add_cell(cell.cell(i, j, False))
            
    '''
    board1.get_cell(1, 2).set_alive(True)
    board1.get_cell(2, 2).set_alive(True)
    board1.get_cell(3, 2).set_alive(True)
    board1.get_cell(3, 1).set_alive(True)
    board1.get_cell(2, 0).set_alive(True)
    '''
    
    
    board1.draw()
    while True:
        iteration += 1
        board1 = board1.update()
        time.sleep(0.5)
        os.system('cls')
        print("Iteration: {}".format(iteration))
        board1.draw()
        
main()