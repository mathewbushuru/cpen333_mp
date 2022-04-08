snakeCoordinates = [(145, 55), (135, 55), (125, 55), (115, 55), (105, 55)]
x_range = range(snakeCoordinates[-1][0] - 10, snakeCoordinates[-1][0])
direction = "Left"
prey_coordinates = (87, 45, 97, 55)
print("Xrange:", x_range)
print("Prey coord ", prey_coordinates[2])
print("snake_coordinates", snakeCoordinates[-1][0])
if direction == "Left" and prey_coordinates[2] in x_range:
    print("LEFT WPRKS")
else:
    print("WE  are in troublke")
