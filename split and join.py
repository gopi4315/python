#for joining of strings in b\w the strings.ex-this is pyhton output wil be this-is-python 
def split_and_join(line):
     list_line = line.split(sep=' ')
     line = "-".join(list_line)
     return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)