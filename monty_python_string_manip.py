a_str=()
a_str=str(a_str)

while count < 80:
    a_str = a_str + "#"
    count += 1
    if count == 80:
        print(a_str)
        break
