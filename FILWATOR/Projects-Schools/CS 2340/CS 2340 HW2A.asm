# Name: karl Azangue				NetID: kka210001
# This program aims to find and display the largest number among three labeled values (n1, n2, n3) stored in memory. The values 
# are loaded into registers, and conditional branches are used to compare them. The program then determines the highest value\
# and stores it in register $s0. Finally, it outputs the highest value to the screen using a system call and saves it in memory
# under the label 'Result'. The program concludes by terminating with a system call. The provided values for n1, n2, and n3 are
# 1, 9, and 50, respectively, resulting in the highest value, 50, being displayed on the screen and stored in memory under
# 'Result' as intended.

	
	
	
	.data 
n1: 	.word	1  	# Creat a label stored in memory called 'n1' in with the value 10
n2:	.word 	9	# Creat a label stored in memory called 'n2' in with the value 13
n3: 	.word	5	# Creat a label stored in memory called 'n3' in with the value 5
Result: .word 		# Creat a label stored in memory called 'Result", will contain the highest value found

	.text
	
main:
	lw $t1, n1		# Load the value from label n1 store in memory and puts it in $t1
	lw $t2, n2		# Load the value from label n2 store in memory and puts it in $t1
	lw $t3, n3		# Load the value from label n3 store in memory and puts it in $t1

	bgt $t1, $t2, checkN1	# Checks ff n1 > n2, if true the program will go to 'checkN1' and check if n1 > n3
	j checkN2		# If the case above is not true, then the program will go to 'checkN2' check if n2 > n3
	
# Program compares value in each register and chooses the highest one
checkN1:
	bgt $t1, $t3, storeN1	# Program checks if n1 > n3, if true the program will go to 'storeN1' and store n1 into s0
	j storeN3		# Else, the program will go to 'storeN3' and store n3 into s0

checkN2:
	bgt $t2, $t3, storeN2	# Program checks if n2 > n3, if true the program will go to 'storeN2' and store n2 into s0
	j storeN3		# Else, the program will go to 'storeN3' and store n3 into s0
	
# Program stores the highest found value into s0
storeN1:
	add $s0, $t1, $zero	# Program store the value in n1 into s0
	j endProgram		# Program jumps to 'endProgram' where the program will be terminated
	
storeN2:
	add $s0, $t2, $zero	# Program store the value in n2 into s0
	j endProgram		# Program jumps to 'endProgram' where the program will be terminated
	
storeN3: 
	add $s0, $t3, $zero	# Program store the value in n3 into s0
	j endProgram		# Program jumps to 'endProgram' where the program will be terminated
	
endProgram: 
	sw $s0, Result		# Program saves the higest value in memory or the label 'Result'
	
	li $v0, 1		# Program outputs the highest value onto the screen
 	move $a0, $s0
	syscall
	
	li $v0, 10		# Program get terminated
	syscall

	
