
'''

>>> merge_meetings([(11,12), (4,8), (3,5), (6,7) , (9,10)])
[(3, 8), (9, 10), (11, 12)]

>>> merge_meetings([(11,12)])
[(11, 12)]

>>> better_merge([(11,12), (4,8), (3,5), (6,7) , (9,10)])
[(3, 8), (9, 10), (11, 12)]
'''

def merge_meetings(meetings):

	meetings = sorted(meetings)

	new_meetings = []
	temp = []
	i=0

	while i < len(meetings):
	    
	    if i == len(meetings) - 1:
	        if temp:
	            new_meetings.append(temp[0])
	        else:
	            new_meetings.append(meetings[i])

	    else:
	        first = temp[0] if temp else meetings[i]
	        second = meetings[i+1]

	        if second[0] > first [1]:
	            #can't merge
	            new_meetings.append(first)
	            del temp[:]
	            
	        else:
	            #can merge
	            temp = [(first[0], max(second[1], first[1]))]

	    i+=1

	return new_meetings

def better_merge(meetings):


	sorted_meetings = sorted(meetings)

	merged_meetings = [sorted_meetings[0]]

	for  curr_start,curr_end in sorted_meetings[1:]:

		prev_start, prev_end = merged_meetings[-1]

		if curr_start > prev_end:
		    #can't merge
		    merged_meetings.append((curr_start, curr_end))
		else:
		    #merge
		    merged_meetings[-1] = prev_start, max(curr_end, prev_end)
	      

	return merged_meetings



if __name__ == '__main__':
	import doctest
	doctest.testmod()

