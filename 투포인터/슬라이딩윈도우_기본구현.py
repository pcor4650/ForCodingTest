data = [1, 2, 3, 4, 5]
window_size = 3

def sliding_window(data, window_size):
    array = []
    for i in range(len(data) - window_size + 1):
        array.append(data[i: i + window_size])
    return array
        
arr = sliding_window(data, window_size)
for x in arr:
    print(x)