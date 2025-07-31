#Name: Karl Azangue
#ID: kka210001
		
		.data
#Beginning Prompt
banner1: 	.asciiz 	"\n\n-----------------------------------------------------\n"
banner2: 	.asciiz 	"          MIPS Car Sensor System Simulation          \n"
banner3: 	.asciiz 	"-----------------------------------------------------\n\n"
newLine: 	.asciiz 		"\n"
#buffer: 	.space 		1
 

#End/Start Prompts
enterStart:	.asciiz 	"\nPress Enter to Start the Simulation...\n"
simStarted: 	.asciiz 	"[Simulation Started]\n\n"
exitAbort:	.asciiz		"\nSimulation aborted\n"


#Inputs prompt Texts
enterInitial:	.asciiz 	"Please enter the initial sensor readings:\n\n"
tempPrompt: 	.asciiz 	"Enter the temperature (in Fahrenheit): "
speedPrompt: 	.asciiz 	"Enter the speed (in mph): "
fuelPrompt: 	.asciiz 	"Enter the fuel level (in gallons): "


#Sensor Readings
endingReading:	.asciiz 	"Sensor Readings:\n"
tempReading:	.asciiz		"Temperature: "
speedReading:	.asciiz		"Speed: "
fuelReading:	.asciiz		"Fuel Level: "
moreReading:	.asciiz		"\nMore sensors reading? enter 1 for yes and 0 for no: "

#Warning Messages
senReading:	.asciiz 	"\n\n                        Sensor Readings:\n"
tempLow: 	.asciiz 	"\n[WARNING] Temperature is below expected value of 34°F.\n"
tempHigh: 	.asciiz 	"\n[WARNING] Temperature is above expected value of 100%.\n"
speedHigh: 	.asciiz 	"\n[WARNING] Speed is above expected value of 65 mph.\n"
speedLesZero:	.asciiz 	"[Invalid] Speed can not be less than 0, TRY AGAIN.\n"
fuelLow: 	.asciiz 	"\n[WARNING] Fuel Level below expected level of 10%.\n"
fuelToHigh:	.asciiz 	"[Invalid] fuel cannot be higher than 15 gallons, TRY AGAIN.\n"
fuelToLow: 	.asciiz		"[Invalid] fuel cannot be less than 0 gallons, TRY AGAIN.\n"
tempOK:		.asciiz		"Temperature is fine\n"
speedOK:	.asciiz		"Speed is fine\n"
fuelOK:		.asciiz		"Fuel is fine\n"
   
   
		.text 
main:

		# The following programs are going to display the banners on to the screen
		li $v0, 4  			# Put the number 4 into register v0. 
		la $a0, banner1 		# Displays "--------..."
		syscall 
		
		li $v0, 4  			# Put the number 4 into register v0. 
		la $a0, banner2 		# Displays "MIPS Car Sensor System Simulation"
		syscall 	
		
		li $v0, 4  			# Put the number 4 into register v0. 
		la $a0, banner3 		# Displays "--------..."
		syscall 			
			
			
    		 		 		
startSimulation:
# Simulation Starts
   		# Print the simulation started message
    		li $v0, 4          		# Simulations starts romtp
    		la $a0, simStarted    		# Displays a message stating tha simulation has started
    		syscall
    		
    		# The following program displys the "please enter the initial sensor....." 
		li $v0, 4              		
		la $a0, enterInitial     	# Displays the message on to screen
		syscall
   			
   					
# User Input
		# The following program gets the user inputs 
		li $v0, 4              		# Syscall code for print string
		la $a0, tempPrompt     		# Displays the prompt for temperature
		syscall

		li $v0, 5              		# Syscall code for read integer
		syscall
		move $s0, $v0          		# Store temperature in $t0
		
		
speed: # This will be used in case space is less than 0
   		#---------------------------------------
		li $v0, 4             		# Syscall code for print string
		la $a0, speedPrompt    		# Displays the prompt for speed
		syscall

		li $v0, 5              		# Syscall code for read integer
		syscall
		move $s1, $v0          		# Store speed in $t1
		bltz $s1, printSpeedLsZero
				
 gallons: # Used in cased fuel is more than 15 or more than zero
   		#---------------------------------------
		li $v0, 4              		# Syscall code for print string
		la $a0, fuelPrompt     		# Displays the prompt for fuel
		syscall

		li $v0, 5              		# Syscall code for read integer
		syscall
		move $s2, $v0          		# Store fuel gallons in $t2
		li $t3, 15			# Max fuel capacity is 15 gallons
		bgt $s2, $t3, fuelHigh		# Branch to 'fuelHigh' if the inputted temperature is higher than 15
		bltz $s2, fuelInvalid		# Branch to 'fuelInvalid' if the inputted temperature is less than 0
   		
   		
   		
#-----------------------------------COMPUTATION
#Here is where inputs are tested

		# Temperature
		li $t0, 34			# Load the Minimum temperature in $t0
    		li $t1, 100			# Load the Maximum temperature in $t1
		blt $s0, $t0, printLowtemp	# Branch if temperature is below threshold
    		bgt $s0, $t1, PrintHightemp	# Branch if temperature is above threshold
   			
   		li $v0, 4
    		la $a0, tempOK			# Displays this on the screen if temperature is withing normal range
    		syscall
  


speedTest:	
		# Speed
		li $t2, 65
    		bgt $s1, $t2, printSpeedHigh	# Branch if inputted speed is higher than 65
		
		li $v0, 4
    		la $a0, speedOK			# Displays this on the screen if speed is withing normal range
    		syscall
		
		
fuelTest:
		# Fuel				# The following code, convert inputed gallons to percentage 
		li $t5, 10          		# Min fuel is 10 percent
   		mul $t4, $s2, 100   		# $t4 = fuel level in gallons * 100
   		div $t4, $t4, $t3   		# $t4 = ($t4 / $t3) = fuel level percentage
		blt $t4, $t5, fuelLow10
		
		li $v0, 4
    		la $a0, tempOK			# Displays this on the screen if fuel is withing normal range
    		syscall
		j moreInput			# Go to the exit function is everything ran fine, it will be asked to continue or exit
		
		
		
		
		
#---------------------------------------------------------------------------HelperFunctions 
	# ----------temperature
printLowtemp:
		li $v0, 4
    		la $a0, tempLow			# Display a message stating that the iputed temperature is too low
    		syscall
    		j speedTest			# Jumps to the next function (Speed)



PrintHightemp:
		li $v0, 4
    		la $a0, tempHigh		# Display a message stating that the iputed temperature is too low
    		syscall
    		j speedTest			# Jumps to the next function (Speed)



	# ----------Speed
printSpeedHigh: 
		li $v0, 4
    		la $a0, speedHigh		# Display a message stating that the iputed speed is too high
    		syscall
    		j fuelTest			# Jumps to the next function (fuel)


printSpeedLsZero:
   		li $v0, 4
    		la $a0, speedLesZero		# Display a message stating that the iputed speed is less than zero
    		syscall
    		j speed				# Goes back to the speed function so the user can enter a new value



	# ----------fuel
fuelHigh:
		li $v0, 4
    		la $a0, fuelToHigh		# Display a message stating that the iputed fuel is to high
    		syscall
    		j gallons			# Goes back to the gallons function so the user can enter a new value
    		
    		
fuelInvalid:
		li $v0, 4
    		la $a0, fuelToLow		# Display a message stating that the iputed fuel is less than zero
    		syscall
    		j gallons			# Goes back to the gallons function so the user can enter a new value
    		
fuelLow10:
		li $v0, 4
    		la $a0, fuelLow
    		syscall
	
		
			
#---------------------------------------------------------------------------WhileLoop Or Exit Function 
moreInput:	
		li $v0, 4             		# Syscall code for print string
		la $a0, moreReading    		# Displays the prompt for moreReading
		syscall


		li $v0, 5              		# Syscall code for read integer
		syscall
		move $s3, $v0          		# Store the inputtedValue in $t3
		bnez $s3, startSimulation

		
    		li $v0, 4
    		la $a0, exitAbort		# Display a message stating that the program was aborted
    		syscall
    		
		li $v0, 10			# Program get terminated
		syscall
		
		
		
		
		
		
		
		
	
		
	
