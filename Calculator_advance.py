print ("Welcome to my Calculator")
print (' ')
loop = 1
opperand = 0
while loop == 1:
	opperand = input('Press'+'\n'+
'A for Addition'+'\n'+
'S for Substraction'+'\n'+
'M for Multiplication'+'\n'+
'D for Division'+'\n'+
'B for Square'+'\n'+
'SR for Square root'+'\n'+
'Q for Quit'+'\n'+
':::::---')
	print (' ')
	if opperand == ('A') or opperand == ('a'):
		a = int(input('1st Number::---'))
		b = int(input('2nd Number::---'))
		print (' ')
		print (a+b)
		print (' ')
	elif opperand == ('S') or opperand == ('s'):
		a = int(input('1st Number::---'))
		b = int(input('2nd Number::---'))
		print (' ')
		print (a-b)
		print (' ')
	elif opperand == ('M') or opperand == ('m'):
		a = int(input('1st Number::---'))
		b = int(input('2nd Number::---'))
		print (' ')
		print (a*b)
		print (' ')
	elif opperand == ('D') or opperand == ('d'):
		a = int(input('1st Number::---'))
		b = int(input('2nd Number::---'))
		print (' ')
		print (a/b)
		print (' ')
	elif opperand == ('B') or opperand == ('b'):
		a = int(input('Number::---'))
		b = 2
		print (' ')
		print (a**b)
		print (' ')
	elif opperand == ('SR') or opperand == ('Sr') or opperand == ('sr') or opperand == ('sR'):
		a = int(input('Number::---'))
		b = 0.5
		print (' ')
		print (a**b)
		print (' ')
	elif opperand == ('Q') or opperand ==('q'):
		loop = 0
print ("THANK YOU")
print (' ')
print ("VISIT AGAIN")
