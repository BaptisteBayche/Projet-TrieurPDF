def get_path():
    with open("option.txt",'r') as file:
        return file.read()

def set_path(path):
    with open("option.txt","w") as file:
        file.write(path)




if __name__=='__main__':
    set_path('D:\Documents\pdf')
    print(get_path())