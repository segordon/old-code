#Prompt the user for the number of inches that have fallen.
#Find the volume (in cubic feet) of water (where volume = depth * area)
#Convert the volume (in cubic feet) to gallons.

inches_str = input("How many inches of rain have fallen: ")
inches_float = float(inches_str)
volume = (inches_float/12)*43560
gallons = volume * 7.48051945
print(inches_int," in. of rain on 1 acre is", gallons, "gallons")
