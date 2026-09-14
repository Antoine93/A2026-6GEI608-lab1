import json

#filename = str(input("Nom du fichier : "))
filename = str("input-Ex1\\Ex1-1.txt")
readfile = open(filename, "r")

lines = readfile.readlines() 

str_lines_matrix = [[col for col in range(3)] for row in range(3)]
lines_matrix = [[col for col in range(3)] for row in range(3)]

for i in range(3):
    lines[i] = lines[i].replace("\n","")

    str_lines_matrix[i] = lines[i].split("\t")
    
    for j in range(3):
        if str_lines_matrix[i][j].isdigit():
            lines_matrix[i][j] = str_lines_matrix[i][j]
        else:
            lines_matrix[i][j]=0

    

print(lines_matrix)
