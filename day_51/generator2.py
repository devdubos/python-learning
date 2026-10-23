import re
def log_reader(file_path):
    with open (file_path,'r', encoding='utf-8') as file:
        for line in file:
            yield line
def log_filter(generator_fileread):
    for line in generator_fileread:
        if "WARNING" in line or "ERROR" in line:
            yield line
def log_batcher(filtered_stream):
    box_2 = []
    how = 0
    for line in filtered_stream:
        if how == 2:
            yield box_2
        how += 1
        box_2.append(line)
    yield box_2




file_path = ('day_51/server.log')



file_read = log_reader(file_path)
file_filter = log_filter(file_read)
filtered_stream = log_batcher(file_filter)
while True:
    line = next(filtered_stream,None) 
    if line is None:
        raise Exception('Endlines')
    print(line)


