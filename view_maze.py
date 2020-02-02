import csv

def View_Maze():
    
    with open('maze.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
        
