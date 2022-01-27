import argparse
import random as ra

MAX_VALUE = (2**12)-1

def create_binary_file(filename:str, vars:list):
    file = open(filename + ".bin", "wb")
    size = len(vars)
    i = 0
    while i < size:
        binary = '{0:012b}'.format(vars[i]) + '{0:012b}'.format(vars[i+1])
        triple_byte = []
        triple_byte.append(int(binary[0:8], 2))
        triple_byte.append(int(binary[8:16], 2))
        triple_byte.append(int(binary[16:24], 2))
        file.write(bytearray(triple_byte))
        i+=2
    file.close()

def create_text_file(filename:str, vars:list):
    file = open(filename + ".txt", "w")
    if vars[-1] == 0:
        vars.pop()
    size = len(vars)
    sorted_vars = sorted(vars, reverse=True)
    if size > 32:
        size = 32
    i = 1
    file.write('--Sorted Max 32 Values--\n')
    while i <= size:
        file.write(str(sorted_vars[-i]))
        file.write("\n")
        i+=1
    file.write('--Last 32 Values--\n')
    i = size
    while i > 0 :
        file.write(str(vars[-i]))
        file.write('\n')
        i-=1
    file.close()

def simple_test():
    filename = "simple_test"
    vars = [3,1,2,5,6,4]
    create_binary_file(filename, vars)
    create_text_file(filename, vars)

def zero_at_end():
    filename = "zero_at_end"
    vars = [123,76,25,86,91,0]
    create_binary_file(filename, vars)
    create_text_file(filename, vars)

def main():
    parser = argparse.ArgumentParser(description='Creates binary files with randomish variables that are a 12 bits wide.')
    simple_test()
    zero_at_end()

if __name__ == "__main__":
    main()