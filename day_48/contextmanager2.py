# file = open('day_48/data.txt','r')
# try:
#     print(file.read())
# finally:
# #     file.close()

# with open('day_48/data.txt','r') as file:
#     print(file.read())


class FileOpener:
    def __init__(self,file_path:str, mode:str) -> None:
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self.file


    def __exit__(self, exc_type, exc, tb):
        self.file.close()
        return False

with FileOpener('day_48/data.txt','r') as file:
    print(file.read())
    raise ValueError("ASDFASF")