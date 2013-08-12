import csv
morse_file = open("morse.txt", "r")
reader = csv.reader(morse_file)
for row in reader:
    print(row)
