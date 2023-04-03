# Define the nested list representing the store-rooms and boxes
rooms = [[3, 8, 2, 6], [5, 1, 9, 4], [7, 2, 6, 3]]

# Initialize variables to keep track of the box with the most apples and the total number of apples
max_apples = 0
total_apples = 0

# Iterate through each box to find the one with the most apples and calculate the total number of apples
for room in rooms:
    for box in room:
        total_apples += box
        if box > max_apples:
            max_apples = box

# Calculate the average number of apples per box
num_boxes = len(rooms) * len(rooms[0])
avg_apples = total_apples / num_boxes

# Print the results
print("Box with the most apples:", max_apples)
print("Average number of apples per box:", avg_apples)
