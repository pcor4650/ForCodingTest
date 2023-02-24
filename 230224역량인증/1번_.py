def CalLargestBlock(id_ignore):
	max_block_size = 0
	pre = ID[0]
	if pre == id_ignore: cur_size = 0
	else: cur_size = 1
	
	for i in range(1, N):
		if ID[i] == pre: cur_size += 1
		else: 
			if ID[i] == id_ignore:
				continue
			if ID[i-1] == id_ignore and ID[i] == pre:
				cur_size += 1
				
			else:
				pre = ID[i]
				cur_size = 1

		if max_block_size < cur_size: max_block_size = cur_size
	return max_block_size