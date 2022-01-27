import os
import argparse
import tkinter as tk
from tkinter import filedialog
import datetime as dt

EXE = None

def getExe():
    parser = argparse.ArgumentParser(description='Assesses the assesment submitted for employment.')
    parser.add_argument('-e', '--executable', type=str, required=False, help="Executable submission.")
    args = parser.parse_args()
    if args.executable:
        EXE = args.executable
    else:
        print("Please select the executable file to be assessed.")
        root = tk.Tk()
        root.withdraw()
        EXE = filedialog.askopenfilename()

def main():
    getExe()


if __name__ == "__main__":
    main()