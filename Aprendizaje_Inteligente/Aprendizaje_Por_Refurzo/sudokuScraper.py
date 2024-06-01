import pandas as pd 
import numpy as np
import csv
from time import sleep
import sys
import get_puzzle
import parameters

params = parameters.params

def tryGetPuzzle(retries):
    global filename
    global curr_params

    if retries > 20:
        return
    try:
        with open(filename, 'a') as f:
            global i
            writer = csv.writer(f)

            while i <= no_puzzles:
                puzzle, solution = get_puzzle.
