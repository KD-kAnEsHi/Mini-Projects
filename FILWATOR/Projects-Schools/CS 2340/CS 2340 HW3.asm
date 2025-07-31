		.data
arraySize: 	.asciiz "Enter many numbers you are gonna enter: "
arrayValues: 	.asciiz "\nEnter the numbers one by one: \n"
sorted: 	.asciiz "\nNumbers in ascending order: \n"
newline: 	.asciiz " "

		.text

	# Syscall, prompts the user to enter the amount of numbers they will enter
	li $v0, 4
	la $a0, arraySize
	syscall

	# Syscall, stores the values entered by the user
	li $v0, 5
	syscall
	move $s0, $v0  			# Stores the user input into the register '$s0'

	# Syscall, Allocate memory for the array based off of the size input
	li $a0, 4  			# Every integer in the array has 4 bytes
	mul $a0, $a0, $s0  		# Calculate the total size allocated for the array
	li $v0, 9  			# Allocate memory in the heap, using sbrk
	syscall
	move $s1, $v0  			# Store the base address of the array in the register '$s1'
	move $s4, $s1  			# Store the base address, This address will be used to parse through the array when printing

	# Syscall, prompts the user to enter the array elements one after another
	li $v0, 4
	la $a0, arrayValues
	syscall

# --------------------------------------Input in Array Function----------------------------------------------------------------------
	li $t0, 0  			# Counter = 0, initialize the loop counter '$t0' to 0

loopInput:
	bge $t0, $s0, sortFunc  	# Counter >= Size, if counter >= arraySize, go to the sort function
	li $v0, 5  			# Syscall, lets the user input more values until array size is reached
	syscall
	sw $v0, 0($s1)  		# Array[size] = userInput, store the inputted integer at the current array index
	addi $s1, $s1, 4  		# Array[size+1], move to the next array index
	addi $t0, $t0, 1  		# Counter++, increment the array counter by 1
	j loopInput

# --------------------------------------Sorting Function----------------------------------------------------------------------------
sortFunc:
	move $a0, $s4  			# $a0 = address of the array
	move $a1, $s0  			# $a1 = count (array size)
	jal sort_numbers_ascending  	# Call the sort_numbers_ascending function

	# Print the sorted numbers
	li $v0, 4
	la $a0, sorted
	syscall

	move $t0, $s0  			# $t0 = count
	move $t1, $s4  			# $t1 = address of the array
print_loop:
	lw $a0, 0($t1)  		# $a0 = array[i]
	li $v0, 1
	syscall  			# print array[i]

	li $v0, 4
	la $a0, newline
	syscall  			# print newline

	addi $t1, $t1, 4  		# increment array pointer
	addi $t0, $t0, -1  		# decrement count
	bgtz $t0, print_loop
	li $v0, 10  			# exit syscall code
	syscall  			# exit

	sort_numbers_ascending:
	addi $sp, $sp, -20  		# allocate space on the stack
	sw $ra, 16($sp)  		# save $ra
	sw $s0, 12($sp)  		# save $s0
	sw $s1, 8($sp)  		# save $s1
	sw $s2, 4($sp)  		# save $s2
	sw $s3, 0($sp) 	 		# save $s3

	move $s0, $a0  			# $s0 = address of the array
	move $s1, $a1 	 		# $s1 = count

	addi $s2, $zero, 0  		# j = 0
ouFor:
	bge $s2, $s1, exit2  	# if j >= count, goto end_outer_loop

	addi $s3, $s2, 1  		# k = j + 1
inFor:
	bge $s3, $s1, exit1	  	# if k >= count, goto end_inner_loop

	mul $t0, $s2, 4  		# $t0 = j * 4
	add $t1, $s0, $t0  		# $t1 = address of array[j]
	lw $t2, 0($t1)  		# $t2 = array[j]
	mul $t3, $s3, 4  		# $t3 = k * 4
	add $t4, $s0, $t3  		# $t4 = address of array[k]
	lw $t5, 0($t4)  		# $t5 = array[k]
	bgt $t2, $t5, swap  		# if array[j] > array[k], goto swap

	addi $s3, $s3, 1  		# k++
	j inFor  			# goto inner_loop
swap:
	sw $t5, 0($t1)  		# array[j] = array[k]
	sw $t2, 0($t4)  		# array[k] = temp
	addi $s3, $s3, 1  		# k++
	j inFor  			# goto inner_loop
	
exit1:
	addi $s2, $s2, 1  		# j++
	j ouFor  			# goto outer_loop
	
exit2:
	lw $ra, 16($sp)  		# restore $ra
	lw $s0, 12($sp)  		# restore $s0
	lw $s1, 8($sp)  		# restore $s1
	lw $s2, 4($sp)  		# restore $s2
	lw $s3, 0($sp)  		# restore $s3
	addi $sp, $sp, 20  		# deallocate space on the stack
	jr $ra  			# return