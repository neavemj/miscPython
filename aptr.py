#!/usr/bin/env python

# Apnea training tables on the command line
# Matthew J. Neave 21.06.16

import sys
import time
import argparse
import random

parser = argparse.ArgumentParser("apnea training")

parser.add_argument("-t", "--training_type", type = str,
        nargs = 1, help = "must be either co2 or o2", required=True)
parser.add_argument("-b", "--base_time", type = int, default = 90,
        nargs = "?", help = "default: 90, should be in seconds", const=1)
parser.add_argument("-s", "--step_time", type = int, default = 10,
        nargs = "?", help = "default: 10, should be in seconds", const=1)

args = parser.parse_args()

train_type = args.training_type[0]
base_length = args.base_time
step_time = args.step_time

def check_inputs(train, base, step):
    if train == "co2":
        final_time = base - (step * 7) 
        if final_time < 0:
            print "error: the input base and step cannnot be completed in 8 reps"
            quit() 

def display(secs, char):
    secs = secs - 1
    if secs < 6:
        print secs
    elif secs % 2 == 0:
        print char * (secs / 2)

def count_down(training, base, step):
    
    check_inputs(training, base, step)

    if training == "co2":
        print "\n~ co2 tables ~"

    elif train_type == "o2":
        print "\n~ o2 tables ~"

    else:
        print "first argument should be co2 or o2"
    
    prep_time = hold_time = base

    for rep in range(1, 9):
        print "\nRep", rep, "\n"
        print "Preparation:", prep_time
        for seconds in range(prep_time, 0, -1):
            time.sleep(1)
            display(seconds, "-")
        print "hold:", hold_time
        for seconds in range(hold_time, 0, -1):
            time.sleep(1)
            display(seconds, "*")

        if training == "co2":
            prep_time -= step 
        elif trining == "o2":
            hold_time += step

    finish_list = ["success!", "nice!", "good job!", "done!", "completed!",
    "excellent!", "easy!", "yeh!", "great!"] 
    print "\n", finish_list[random.randint(0, len(finish_list))], "\n"

count_down(train_type, base_length, step_time)
