row1 = ["😀", "😀", "😀"]
row2 = ["😀", "😀", "😀"]
row3 = ["😀", "😀", "😀"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
column = position[0]
column =int(column) - 1
row = position[1]
row = int(row) - 1
# selected_row = map[row]
# selected_row[column] = "X"
map[row][column] = "X"

print(f"{row1}\n{row2}\n{row3}")
