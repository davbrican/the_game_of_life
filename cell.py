class cell:
    def __init__(self, x = 0, y = 0, alive = False):
        self.x = x
        self.y = y
        self.alive = alive
        
    def __str__(self):
        return "Cell at ({},{}) is {}".format(self.x, self.y, self.alive)
    
    
    # 1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    # 2. Any live cell with two or three live neighbours lives on to the next generation.
    # 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    # 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    def update(self, board):
        neighbours = self.get_neighbours(board)
        alive_neighbours = []
        new_cell = cell(self.x, self.y, self.alive)
        for i in neighbours:
            if i != None:
                if i.alive == True:
                    alive_neighbours.append(i)
        if self.alive == True:
            if len(alive_neighbours) < 2 or len(alive_neighbours) > 3:
                new_cell.set_alive(False)
            elif len(alive_neighbours) == 2 or len(alive_neighbours) == 3:
                new_cell.set_alive(True)
        elif self.alive == False:
            if len(alive_neighbours) == 3:
                new_cell.set_alive(True)
            else:
                new_cell.set_alive(False)  
        
        return new_cell
            
    def draw(self):
        if self.alive == True:
            return "■"
        else:
            return "□"
    
    def get_neighbours(self, board):
        return board.get_neighbours(self.x, self.y)
    
    def set_alive(self, alive):
        self.alive = alive