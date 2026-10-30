
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
            box_2 = []
            how = 0
        how += 1
        box_2.append(line)
    yield box_2
    


# file_path = ('day_51/server.log')



# file_read = log_reader(file_path)
# file_filter = log_filter(file_read)
# filtered_stream = log_batcher(file_filter)
# while True:
#     line = next(filtered_stream,None) 
#     if line is None:
#         raise Exception('Endlines')
#     print(line)


def log_reader(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def log_filter(stream, keyword):
    for line in stream:
        if keyword in line:
            yield line

def log_batcher(stream, batch_size):
    batch = []
    for line in stream:
        batch.append(line)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

if __name__ == '__main__':
    import os

    dummy_file = 'demo_server.log'
    with open(dummy_file, 'w', encoding='utf-8') as f:
        f.write("[INFO] System start\n")
        f.write("[WARNING] Low disk space\n")
        f.write("[INFO] User login\n")
        f.write("[ERROR] Database connection failed\n")
        f.write("[WARNING] High memory usage\n")
        f.write("[INFO] System stop\n")

    print("--- Execution Result ---")
    
    file_stream = log_reader(dummy_file)
    filtered_stream = log_filter(file_stream, "WARNING")
    batched_stream = log_batcher(filtered_stream, 2)

    for batch in batched_stream:
        print("Received batch:", batch)

    if os.path.exists(dummy_file):
        os.remove(dummy_file)




        