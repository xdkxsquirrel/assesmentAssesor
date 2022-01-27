import os
import subprocess
import argparse
import tkinter as tk
from tkinter import filedialog
from datetime import datetime as dt
import filecmp as fc
import itertools as it
import binaryCreator

EXE = None
CLEAN = False

def cleanup():
    test_names = open('test_names.txt', 'r')
    for test_name in test_names:
        if test_name != "":
            if os.path.exists(test_name[0:-1] + ".txt"):
                os.remove(test_name[0:-1] + ".txt")
            if os.path.exists(test_name[0:-1] + ".bin"):
                os.remove(test_name[0:-1] + ".bin")
            if os.path.exists(test_name[0:-1] + "_submission.txt"):
                os.remove(test_name[0:-1] + "_submission.txt")
    test_names.close()

def get_exe():
    global EXE
    global CLEAN
    parser = argparse.ArgumentParser(description='Assesses the assesment submitted for employment.')
    parser.add_argument('-e', '--executable', type=str, required=False, help="Executable submission.")
    parser.add_argument('-d', action='store_true', help="Delete all created files.")
    args = parser.parse_args()
    if args.d:
        CLEAN = True
    if args.executable:
        EXE = args.executable
    else:
        print("Please select the executable file to be assessed.")
        root = tk.Tk()
        root.withdraw()
        EXE = filedialog.askopenfilename()

def run_script(args:list) -> list:
    ret = [ 0, "no error"]
    try: 
        ret[0] = subprocess.check_call(args)
    except subprocess.CalledProcessError as e:
        ret[1] = e.output
    return ret

def print_txts(test_name:str):
    submission = open(test_name + '_submission.txt', 'r')
    correct = open(test_name + '.txt', 'r')
    print("**SUBMISSION**              **CORRECT_OUTPUT**      ")
    for submission_line, correct_line in it.zip_longest(submission, correct):
        if submission_line is None:
            print(f'{" ":<24}' + "    " + f'{correct_line[0:-1]:<24}')
        elif correct_line is None:
            print(f'{submission_line[0:-1]:<24}' + "    " + f'{" ":<24}')
        else:
            print(f'{submission_line[0:-1]:<24}' + "    " + f'{correct_line[0:-1]:<24}')
    submission.close()
    correct.close()

def run_test(test_name:str):
    args = [EXE, test_name + ".bin", test_name + "_submission.txt"]
    start_time = dt.now()
    returned = run_script(args)
    if returned[1] != "no error":
        print(test_name + " hard faulted.")
        print(returned[0])
        print(returned[1])
        print()
        print()
    else:
        end_time = dt.now()
        time_delta = end_time - start_time
        if fc.cmp(test_name + ".txt", test_name + "_submission.txt", shallow = False):
            print(test_name + " passed in " + str(time_delta) + " seconds.")
            print()
            print()
        else:
            print(test_name + " failed in " + str(time_delta) + " seconds.")
            print_txts(test_name)
            print()
            print()

def main():
    get_exe()
    if os.path.exists("test_names.txt"):
        test_names = open('test_names.txt', 'r')
        print()
        for test_name in test_names:
            if test_name != "":
                run_test(test_name[0:-1])
        test_names.close()
        if CLEAN:
            cleanup()
        os.remove("test_names.txt")
    else:
        print("Must run binaryCreatorFirst.")

    

if __name__ == "__main__":
    main()