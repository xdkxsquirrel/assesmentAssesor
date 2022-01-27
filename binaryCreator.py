import argparse
import random as ra

from numpy import number

MAX_VALUE = (2**12)-1

def add_testname(test_name:str):
    file = open("test_names.txt", "a")
    file.write(test_name + "\n")
    file.close()

def create_binary_file(filename:str, vars:list):
    add_testname(filename)
    file = open(filename + ".bin", "wb")
    size = len(vars)
    i = 0
    while i < size:
        if size == 1:
            file.write(bytearray(vars))
        else:
            binary = '{0:012b}'.format(vars[i]) + '{0:012b}'.format(vars[i+1])
            bytes_to_write = []
            bytes_to_write.append(int(binary[0:8], 2))
            bytes_to_write.append(int(binary[8:16], 2))
            bytes_to_write.append(int(binary[16:24], 2))
            file.write(bytearray(bytes_to_write))
        i+=2
    file.close()

def create_text_file(filename:str, vars:list):
    file = open(filename + ".txt", "w")
    if len(vars) == 0:
        file.write('--Sorted Max 32 Values--\n')
        file.write('--Last 32 Values--\n')
    else:
        if vars[-1] == 0:
            vars.pop()
        size = len(vars)
        sorted_vars = sorted(vars, reverse=False)
        if size > 32:
            size = 32
        i = size
        file.write('--Sorted Max 32 Values--\n')
        while i > 0:
            file.write(str(sorted_vars[-i]))
            file.write("\n")
            i-=1
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

def empty_file():
    filename = "empty_file"
    vars = [ ]
    create_binary_file(filename, vars)
    create_text_file(filename, vars)

def one_byte():
    filename = "one_byte"
    vars = [ 33 ]
    create_binary_file(filename, vars)
    create_text_file(filename, vars)

def fifty_vars():
    filename = "fifty_vars"
    value = 358
    vars = [ ]
    number_of_vars = 50
    i = 0
    while i < number_of_vars:
        value = value * i - 52
        while value < 0:
            value += MAX_VALUE
        while value > MAX_VALUE:
            value -= MAX_VALUE
        vars.append(value)
        i+=1
    create_binary_file(filename, vars)
    create_text_file(filename, vars)

def main():
    simple_test()
    zero_at_end()
    empty_file()
    one_byte()
    fifty_vars()

if __name__ == "__main__":
    main()