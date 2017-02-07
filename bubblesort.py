




def bubblesort(in_list):

	if len(in_list) == 0:
		return None
	elif len(in_list) == 1:
		return in_list
	else:

		done = False

		while (not done):

			n_swaps = 0

			for i in range(len(in_list)-1):

				if in_list[i] > in_list[i+1]:
					in_list[i], in_list[i+1] = in_list[i+1], in_list[i]
					n_swaps += 1
			if n_swaps == 0:
				done = True

		return in_list


if __name__ == '__main__':
	
	result = bubblesort([4,1,3,2,7])
	print(result)
