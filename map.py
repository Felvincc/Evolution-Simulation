from species import *
import random

class Statistics():
    def __init__(self):
        pass

class Engine():
    # chunk_dimensions: (x length, y length), spawn_data: (species: initial population)
    def __init__(self, chunk_dimensions: tuple, spawn_data: dict):
        self.chunk_dimensions = chunk_dimensions
        self.map = self.Map(chunk_dimensions)
        self.spawn_data = spawn_data

    def start(self):
        self.species_population = []

   
            
        while(1):
            break
            for organism in self.species_population:
                #organism.assess()
                pass

    class Map():
        def __init__(self, dim):
            x_len = dim[0]
            y_len = dim[1]

            # get values for x axis
            if (dim[0] % 2) == 1:
                self.center_x = (x_len//2) + 1 #half + 1, the increment is to find the true center in an odd number lengthed axis
                self.x_pos_offset = x_len//2    
                self.x_neg_offset = x_len//2
            else:
                self.center_x = x_len//2
                self.x_pos_offset = x_len//2
                self.x_neg_offset = (x_len//2)-1    # half - 1, the decrement is to account for the false center in an odd numbered length, assumes we start from negative (which we do)

            # get values for y axis
            if (dim[1] % 2) == 1:
                self.center_y = (y_len//2) + 1
                self.y_pos_offset = y_len//2
                self.y_neg_offset = y_len//2
            else:
                self.center_y = y_len//2
                self.y_pos_offset = y_len//2
                self.y_neg_offset = (y_len//2)-1

            if(0): #show values for debug
                print(f"center_x={self.center_x}")
                print(f"x_neg_offset={self.x_neg_offset}")
                print(f"x_pos_offset={self.x_pos_offset}")
                print(f"center_y={self.center_y}")
                print(f"y_neg_offset={self.y_neg_offset}")
                print(f"y_pos_offset={self.y_pos_offset}")

            self.center_y = dim[1]//2
             
            self.grid = []
            for x in range(dim[0]):
                self.grid.append([])

                for y in range(dim[1]):
                    self.grid[x].append([])

            
        
            





test = Engine((120,101))
test.start()