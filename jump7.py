for a in range(1,101):
    if a%7==0:
        continue
    elif a in [7,17,27,37,47,57,67,87,97] or (a>70 and a<80):
	continue
    else:
        print(a)
