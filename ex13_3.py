from sys import argv

scriptName, firstNum, secondNum = argv

#firstNum = int(firstNum)
#seconNum = int(secondNum)
#first_Num_Retype = int(raw_input("Please retype the first number:"))
#second_Num_Retype = int(raw_input("Please retype the second number:"))
#print """Your identity has passed,
#                                   1st_Num for the first time is: %d ,
#                                   1st_Num for second time is %d,
#                                   2nd_Num for the second time is:%d.
#""" %(firstNum, first_Num_Retype, secondNum, second_Num_Retype)

first_Num_Retype = raw_input("Please retype the first number:")
second_Num_Retype = raw_input("Please retype the second number:")

print """Your identity has passed,
                                   1st_Num for the first time is: %r ,
                                   1st_Num for second time is %r,
                                   2nd_Num for the first time is: %r,
                                   2nd_Num for the second time is:%r.
""" %(firstNum, first_Num_Retype, secondNum, second_Num_Retype)
