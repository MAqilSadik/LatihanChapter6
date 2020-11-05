#sum
def sum (*bilangan):
    sum = 0

    for data in bilangan :
        sum += data
    return sum

#average
def average (*bilangan):
    sum = 0
    i = 0

    for data in bilangan :
        sum += data
        i += 1

    rata2 = sum/i
    return rata2


#maks
def maks (*bilangan):
    maksimum = 0

    for data in bilangan :
        if data > maksimum :
            maksimum = data
    return maksimum


#min
def min (*bilangan):
    minimum = max(*bilangan)+1

    for data in bilangan :
        if data < minimum :
            minimum = data
    return minimum
