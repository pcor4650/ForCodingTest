data = [1, 2, 3, 4, 5]
window_size = 3

def sliding_window(data, window_size):
    for i in range(len(data) - window_size + 1):
        yield data[i: i + window_size]
        
for window in sliding_window(data, window_size):
    print(window)