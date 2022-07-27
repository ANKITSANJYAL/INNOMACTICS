water_trapped = 0 #initial amount of water trapped
heights = [0,1,0,2,1,0,1,3,2,1,2]

for i in range (len(heights)-1):
	current_bar_height = heights[i]
	max_left = max(heights[0:i]) #maximum left on the heights
	max_right = max(heights[i+1]:len(heights)) #maximum right bar on the right side of the current index
	
	#we can only store the water if the height of the current bar is less than the heights of maximum of right and left
	
	if (curR_bar_height < max_left and curr_bar_height<max_right):
		water_trapped+= min(max_left,max_right)-curr_bar_height



	print("total water trapped: {}".format(water_trapped))
