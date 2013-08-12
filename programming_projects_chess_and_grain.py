## Programming Projects : The invention of chess.
## Add the doubling of 1 , 64 times for the amount of grain ( 1,2,4,8,16,32..)
## At 50mg per grain, How much grain do you have at the end of payment?
## Prompt for an area of a region, output the depth with total grain amount


count_int = 0
sum_int = 0
multiplier_int = 1
total_weight_int = 0

while count_int < 64 :
	sum_int = sum_int + multiplier_int
	multiplier_int = multiplier_int * 2
	count_int = count_int + 1
	#print("multiplier:",multiplier_int,"sum",sum_int,"count",count_int) #Debugging Print

if count_int >= 64 : 
	total_weight_int = sum_int * 50 * 0.000001
	print("The total number of grains is", sum_int)
	print("The total weight of the total amount of grains is",total_weight_int,"kg")
