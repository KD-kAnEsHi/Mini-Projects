#Name: Karl Azangue 			NetID: kka210001
#This MIPS assembly program initializes an array named NUM with values from 1 to 9. It uses two loops to achieve this. The first loop
# iterates through each element in the array, starting from NUM[0], and stores consecutive numbers from 1 to 9 in the array. The 
# second loop then traverses the array again, incrementing each element, and calculates the total sum of all elements in the array,
# storing it in register $s0. Finally, the program outputs the total sum to the console using a system call and terminates. The loops
# and memory manipulations demonstrate basic array handling and arithmetic operations in MIPS assembly.

	.data
NUM: 	.word	0 : 9		# "array" of 9 wordsvalues
size: 	.word 	9		# Size of "array"

	.text
main:
	la $t0, NUM		# $t0 = NUM[0], Load address of the array or address
	li $t1, 0		# Instantiate the register $t0
	la $t2, size		# $t2 = size, Load the address of the size variabl
	lw $t2, 0($t2)		# $t2 = 9, Load the array size
	
# The follwing loop iterate through every value in the array startgin from NUM[0] and adds the number from 1 - 9 into it.	
whileLoop:
	addi $t1, $t1, 1	# $t1++, Increment the value that is going to be store in the array by 1
	sw $t1, 0($t0)		# NUM[i] = #t1, store the value in $t1 into memory
	addi $t0, $t0, 4	# NUM[i+1], Moves to the next value in the array
	addi $t2, $t2, -1	# $t4--, Decrement the loop counter by 1
	bgtz $t2, whileLoop	# Repeats the loop if counter '$t0' is greater than 0
	
	la $t3, NUM		# $t3 = NUM[0], Load address of the array or address
	la $t4, size		# $t4 = size, Load the address of the size variable
	lw $t4, 0($t4)		# $t4 = 9, Load the array size
	
# The following loop makes use of a loop and goes through every value in the array starting from NUM[0] 
#and increment every value in the array. During each iteration the total is stored in the register '$s0'
addLoop:
	lw $t5, 0($t3)		# $t5 = NUM[i], Load the value in memory and stores in the register '$t5'
	add $s0, $s0, $t5 	# $s0 += NUM[i], add the value stored in $t5, into '$s0' the register containg the total value
	addi $t3, $t3, 4	# NUM[i+1], Moves to the next value in the array
	addi $t4, $t4, -1	# $t4--, Decrement the loop counter by 1
	bgtz $t4, addLoop	# Repeats the loop if counter '$t4' is greater than 0
	

#END OF PROGRAM
# The fillowing function is going to ouput the total of every value int the array and exit the program.		
	li $v0, 1		# Program outputs the highest value onto the screen
	move $a0, $s0
	syscall
	
	li $v0, 10		# Program get terminated
	syscall
	

















#	.data
#NUM:	.word	1:8		# Creat an array for 8 integers, initialized to zero

#	.text
#main:
#	add $t0, $t0, $zero	# i = 0, loop counter
#	addi $t4, $t4, 9	# array size
	
	
# The following function will add values 1 - 9 into the array using the loop counter, it will add values in the array starting 
# 1 until the counter reaches 9.
#whileLoop:
#	sll $t1, $t0, 2		# i * 4, program increment between every element in the array (Shifts right)
#	add $t2, $a0, $t1	# $t2 = &array[i], stores the addrres of current location in array into '$t2'
#	addi $t0, $t0, 1	# i = i+1, increment the values loop counter so it can be used added to the array
	
#	sw $t0, 0($t2)		# array[i] = i, add the current value in i, into the array
#	bne $t0, $t4, whileLoop	# Runs while loop if value if i is less than 9
	
	
# The follwing function will increment all of the values in the array starting from the big endian, or right most value the 
# program will start from NUM[8] and add all the values until the counter reacher 0
#	add $t0, $t0, $zero
#addLoop:
#	sll $t1, $t0, 2		# i * 4, program increment between every element in the array (Shifts right)
#	add $t2, $a0, $t1	# $t2 = &array[i], stores the addrres of current location in array into '$t2'
#	addi $t0, $t0, 1	# i = i+1, increment the values loop counter so it can be used added to the array
	
	
#	lw $t5, 0($t2)		# Load the values in the current array address
#	add $s0, $s0, $t5	# add the values in the current array addresss into regs`
#	bgtz $t0, addLoop	# repear if the loop counter is greater than 0
	
	
#END PROGRAM		
#	li $v0, 1		# Program outputs the highest value onto the screen
#	move $a0, $s0
#	syscall
	
#	li $v0, 10		# Program get terminated
#	syscall
