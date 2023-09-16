def printMap(map):
    for row in map:
        print(f"{row}\n")

numCol = int(input("Enter the number of columns for the map: "))
numRow = int(input("Enter the number of rows for the map: "))
ch = '■'
row = list(ch*numCol)
map = []
for x in range(numRow):
    map.append(row.copy())
printMap(map)
coordinates = input("Enter the 2 digit coordinates of the treasure location: ")
col = int(coordinates[0])
row = int(coordinates[1])
map[row - 1][col - 1] = 'x'
printMap(map)
