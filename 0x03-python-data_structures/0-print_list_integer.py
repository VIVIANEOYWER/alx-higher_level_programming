#!/usr/bin/python3

#Python program that demonstrates how to print all integers of a list

# By Viviane A Oywer

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
