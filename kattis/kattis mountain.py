import math

def handle_inpt():
	inpt1 =input()
	segment_accelerationlist = inpt1.split(" ")
	distance_anglelist = []

	for i in range(int(segment_accelerationlist[0])):
		inpt2 = input()
		inpt2 = inpt2.split(" ")
		distance_anglelist.append(inpt2)

	return segment_accelerationlist, distance_anglelist

def calc_velocity(seg_acc, dist_angle):
	acc=0 
	vel = []
	for i in range(int(seg_acc[0])-1,-1,-1):
		acc += float(seg_acc[1])*2*math.cos(math.radians(float(dist_angle[i][1])))*float(dist_angle[i][0])
		vel.append(math.sqrt(acc))

	for i in range(len(vel) -1,-1,-1):
		print(vel[i])

seg_acc, dist_angle = handle_inpt()
calc_velocity(seg_acc, dist_angle)