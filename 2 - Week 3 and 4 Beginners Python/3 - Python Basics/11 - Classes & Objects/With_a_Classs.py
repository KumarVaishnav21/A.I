import datetime

# Class
class CricketPlayer:
    # Properties
    def __init__(self, fname, lname, team, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []
     
    # Method    
    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year
    
    # Method 
    def add_score(self, score):
        self.scores.append(score)
     
    # Method    
    def get_average_score(self):
        return sum(self.scores)/len(self.scores)
    
    # Operator overloading method
    def __lt__(self, other):
        my_score = self.get_average_score()
        other_score = other.get_average_score()
        return my_score < other_score
    
    # method will be used to make a class printable using print() in python
    def __str__(self):
        return f'{self.first_name} {self.last_name}, the cricket player from {self.team}'
    

#object creation        
virat = CricketPlayer('virat', 'kohli', 'India', 1988)
virat.add_score(80)
virat.add_score(100)
virat.add_score(0)

david = CricketPlayer('david', 'warner', 'Australia', 1986)
david.add_score(37)
david.add_score(23)
david.add_score(85)

print(virat.first_name)
print(virat.last_name)
print(virat.get_age())
print(virat.get_average_score())

print(david.first_name)
print(david.last_name)
print(david.get_age())
print(david.get_average_score())

print(virat < david)

print(virat)
print(david)