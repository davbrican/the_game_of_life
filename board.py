class board:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.cells = []
        
    def __str__(self):
        return "Board is {}x{} with {} cells".format(self.width, self.height, len(self.cells))
    
    def update(self):
        new_board = board(self.width, self.height)
        for i in self.cells:
            new_cell = i.update(self)
            new_board.add_cell(new_cell)
        return new_board
    
    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.get_cell(j, i).draw(), end="")
            print()
    
    def get_cell(self, x, y):
        for i in self.cells:
            if i.x == x and i.y == y:
                return i
        return None
    
    def get_neighbours(self, x, y):
        return [self.get_cell(x-1, y-1), self.get_cell(x, y-1), 
                self.get_cell(x+1, y-1), self.get_cell(x-1, y), 
                self.get_cell(x+1, y), self.get_cell(x-1, y+1), 
                self.get_cell(x, y+1), self.get_cell(x+1, y+1)]
    
    def add_cell(self, cell):
        self.cells.append(cell)