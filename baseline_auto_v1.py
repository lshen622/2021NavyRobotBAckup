xmax = 315 # Max x value of camera
ymax = 207 # Max y value of camera
xcenter = xmax/2 # Center of camera x axis
ycenter = ymax/2 # Center of camera y axis

pixy_err = __ # camera input error - dependent on testing
dist_err = __ # distance sensor input error - dependent on testing

dt_speed = __ # Standard forward driving speed for drivetrain 0-1
handle_closed == False # Initalize variable
increment = 1 # Initialize variable

s1init = __ # Initialize servo angles to standard
s2init = __ # Initialize servo angles to standard
s3init = __ # Initialize servo angles to standard
s4init = __ # Initialize servo angles to standard


# pixy2.x_coord(1) = camera input
# pixy2.y_coord(1) = camera input


# x - xcenter / xmax
# or because never reaches xmax
# x - xcenter / (xmax/2)

# (Servo1 rotates, Servo2 controls forward/backward, Servo3 controls up/down, Servo4 is rotate manip, Servo5 is open/close manip)
# Initalize Servo angles
# dist1 is a distance sensor object with the available function distance()

# Following goes inside main



if # Pixy2 sees pre trained door colors - pixy sensor dependent
	
	# Approach Door - Distance sensor dependent
	while dist1.distance() > dist_err
	
		# Control DC motors to center horizontally
		motor.move(dt_speed,(pixy2.x_coord(1) - xcenter) / xmax,0.1)

		# Control Arm motor to center vertically
		current_angle3 += ((pixy2.y_coord(1) - ycenter) / ymax)
		Servo3(current_angle3)
	
	# Manipulate Door handle
	Servo4(tbd) # Claw goes vertical
	Servo2(tbd) # Claw moves forward to put handle inside claw
	Servo5(tbd) # Close claw to grasp handle
	
	while handle_closed == False

		# Raise handle upward while adjusting arm to move forward to continue holding handle
		
		currentangle3 += increment
		Servo3(current_angle3) #Up
		
		currentangle2 += increment
		Servo3(current_angle2) #Extend forward
		
		if current_angle2 == tbd and current_angle3 == tbd
			handle_closed = True

	# Open claw to release handle
	