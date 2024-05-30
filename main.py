"""
main
"""
import os
import sys
from utlis import read_matrix_from_file, add_matrices, subtract_matrices, multiply_matrices, write_matrix_to_file

def main():
    if len(sys.argv) != 1:
        pass
    else:
        print("")
        print("\t\t\t\t********Welcome**********\n")
        print("\t\tplease select an operation\n")
        print("\t\t1-----> Addition\n")
        print("\t\t2-----> Subtraction\n")
        print("\t\t3-----> multiplication\n")

        response = None
        operations = {1: add_matrices, 2: subtract_matrices, 3: multiply_matrices}

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

        file1 = input("please enter the path to the first matrix file: ")
        file2 = input("please enter the path to the second matrix file: ")
        try:
            matrix1 = read_matrix_from_file(file1)
            matrix2 = read_matrix_from_file(file2)
        except FileNotFoundError:
            print("please provide a valid path")
            return

        result = operations.get(response)(matrix1, matrix2)
        write_matrix_to_file(result)


main()



