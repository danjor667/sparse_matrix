"""
main
"""
import os

from utlis import read_matrix_from_file
print("")
print("\t\t\t\t********Welcome**********\n")
print("\t\tplease select an operation\n")
print("\t\t1-----> Addition\n")
print("\t\t2-----> Subtraction\n")
print("\t\t3-----> multiplication\n")


response = None

while True:
    response = input()
    try:
        response = int(response)
        if response in (1, 2, 3):
            break
        else:
            print("please select an operation from the one above")
    except ValueError:
        print("please chose between 1 and 3")

if __name__ == "__main__":
    dir = "sample_input_for_students"
    for file in os.listdir(dir):
        print(file)
        read_matrix_from_file("sample_input_for_students/"+file)

