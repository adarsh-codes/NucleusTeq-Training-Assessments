import os
import sys

def list_files_in_cwd():
    print("Files and directories in current working directory:")
    for item in os.listdir('.'):
        print(f"- {item}")

def show_command_line_args():
    print("\nCommand-line arguments:")
    for idx, arg in enumerate(sys.argv):
        print(f"Argument {idx}: {arg}")

if __name__ == "__main__":
    list_files_in_cwd()
    show_command_line_args()
