import sqlite3
import random
import time



class Simplespecies():
    def __init__ (self, seed):
        self.seed = seed
        self.nutrition = 1
        self.speed_expovariate = random.expovariate(1)
        self.hunger = 0.5

        self.boldness = 1
        self.aggresiveness = 1
        self.speed = random.expovariate(self.speed_expovariate) + 5
        self.heat_cycle = 0 #tba


class Species():

    def __init__(self, seed):
        self.seed = seed
        random.seed(self.seed)
        self.health_expovariate = random.expovariate(1)
        self.speed_expovariate = random.expovariate(1)
        self.hunger = 0.5

        self.boldness = random.random()
        self.aggresiveness = random.random()
        self.cosmetic = random.random()
        self.health = random.expovariate(self.health_expovariate) + 5
        self.nutrition = self.health
        self.speed = random.expovariate(self.speed_expovariate) + 5
        self.heat_cycle = 0 #tba

    def __str__(self):
        return f"HP:{self.health},SPD:{self.speed}"

    def assess(self, environment: tuple): # 0: audio | 1: sight | 3: arms-reach interaction
        pass


    def attraction(self, attraction_seed: float):
        pass


    def call(self, call_seed: float):
        pass
    

    def action(self, action_seed: float):
        pass

    def attack(self, creature_id: int):
        pass

def testing():
    counter = 0

    while(1):
        counter = counter + 1
        seed = random.random()
        test_species = Species(seed)
        
        print(f"counter: {counter}")
        print(f"seed: {seed}")
        print(f"health expovariate: {test_species.health_expovariate}")
        print(f"speed expovariate: {test_species.speed_expovariate}")
        print(f"health: {test_species.health}")
        print(f"speed: {test_species.speed}")
        time.sleep(1)




'''
Engine:
    -tracks all species in play
    -phases
        -assessment phase
        -movement phase
        -action phase



Species:
    -Attributes (personality traits)
        -timid <-> bold (likelihood to act, float: 0-1)
        -calm <-> aggresive (exaguration of action float: 0-1)
        -cosmetic: genetic seed (non-linear attraction function)
        -health: non negative integer
        -hunger
        -heat cycle

    -Actions (Calls, Attack, Mate)
        -Calls: variable amount, triggers reaction, mimicry
        -Attack: strength (none negative integer 0 -> infinite )

    -detection range (Hearing, Sight, arms-reach)
        -hearing: detects calls of same species and different species, different species may mimic
        -sight: detects everything within camoflauge detection
        -arms-reach: intimate interactions

    - Assessment (reaction to: different calls,)
        -hearing:
    

'''


