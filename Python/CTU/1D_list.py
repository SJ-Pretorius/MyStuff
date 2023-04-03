#Melissa Approved!
#my_signature_print()
print()

#lists
metals = ['Silver','Zinc','Titanium','Lead','Iron','Tungsten','Aluminium','Nickel','Tantalum','Copper']
melting_points = [1452, 961, 1768, 327, 1538, 3020, 660, 1535, 3422, 1728]

#highest
highest_melting_point = max(melting_points)
highest_melting_point_metal = metals[melting_points.index(highest_melting_point)]
print(f"The metal with the highest melting point is {highest_melting_point_metal} with {highest_melting_point} C.")

#lowest
lowest_melting_point = min(melting_points)
lowest_melting_point_metal = metals[melting_points.index(lowest_melting_point)]
print(f"The metal with the highest melting point is {lowest_melting_point_metal} with {lowest_melting_point} C.")

#avg
average_melting_point = sum(melting_points) / len(melting_points)
print(f"The average melting point of the metals is {average_melting_point} C.")

#my_signature_print()
print()