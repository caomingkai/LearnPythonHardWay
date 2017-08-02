def create_lis(right_boundry,increment):
    i = 0
    numbers = []

    while i < right_boundry:
        # print "At the top i is %d" %i
        numbers.append(i)

        i +=increment
        # print "Numbers now: ", numbers
        # print "At the bottom i is %d" % i


        # print "The numbers: "
        #
        # for num in numbers:
        #     print num
    return numbers

def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b
