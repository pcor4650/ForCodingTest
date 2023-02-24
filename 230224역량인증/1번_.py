def CalLargestBlock(id_ignore):
	max_block_size = 0
	pre = ID[0]														# 삽입
	if pre == id_ignore: cur_size = 0								# 수정
	else: cur_size = 1												# 수정
	
	for i in range(1, N):
		if ID[i] == pre: cur_size += 1								# 수정
		else: 														# 삽입
			if ID[i] == id_ignore:									# 삽입
				continue											# 삽입
			if ID[i-1] == id_ignore and ID[i] == pre:				# 삽입
				cur_size += 1										# 삽입
				
			else:													# 삽입
				pre = ID[i]											# 삽입
				cur_size = 1

		if max_block_size < cur_size: max_block_size = cur_size
	return max_block_size