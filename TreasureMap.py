def printMap(map):
    for row in map:
        print(f"{row}\n")

#row1 = row2 = row3 = ['■', '■', '■']
row1 = ['■', '■', '■']
row2 = ['■', '■', '■']
row3 = ['■', '■', '■']
map = [row1,row2,row3]
printMap(map)
coordinates = input("Enter the 2 digit coordinates of the treasure location: ")
col = int(coordinates[0])
row = int(coordinates[1])
map[row - 1][col - 1] = 'x'
printMap(map)
