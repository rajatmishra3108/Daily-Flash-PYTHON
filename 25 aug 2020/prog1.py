gloves = [35, 30, 25, 40, 50, 20]
masks = [50, 60, 30, 70, 40, 90]

masks.sort()

for i in gloves :

    for j in masks :

        if i + j <= 90 :
            print(i + j, end = " ")

        else :
            break

    print()
