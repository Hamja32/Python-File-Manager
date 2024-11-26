import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"File name {filename} created successfully !!")
    except FileExistsError:
        print(f"File {filename} is already exists !!")
    except Exception as E:
        print("Anonymous error")

def viewAllFile():
    files = os.listdir()
    if not files:
        print("No files found")
    else:
        print("Files in directory")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted")
    except FileNotFoundError:
        print(f"{filename} does'nt exist")
    except Exception as E:
        print(f"An Anonymous error")

def edit_file(filename):
    try:
        with open(filename,'a')as f :
            content = input("Enter data to file : ")
            f.write(content + '\n')
            print(f"Content added to {filename} Successfully")
    except FileNotFoundError:
        print(f"File {filename} is not found")
    except Exception as E :
        print("An Anonymous error")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"Content of {filename} : \n {content}")
    except FileNotFoundError:
        print(f"{filename} dones'nt exits")
    except Exception as E:
        print(f"An Anonymous error")


def main():
    while True:
        print("\nFILE MANAGEMENT APP")
        print("................................")
        print("1: CREATE a file")
        print("2: VIEW ALL file")
        print("3: DELETE a file")
        print("4: READ a file")
        print("5: EDIT a file")
        print("6: EXIT ")
        print("................................\n\n")
        choice = input("Enter your choice (1-6) = ")
        if choice=='1':
            filename = input("Enter file name to create : ")
            create_file(filename)
        elif choice =='2':
            viewAllFile()
        elif choice =='3':
            filename = input("Enter file name to delete : ")
            delete_file(filename)
        elif choice =='4':
            filename = input("Enter file name to read : ")
            read_file(filename)
        elif choice =='5':
            filename = input("Enter file name to edit : ")
            edit_file(filename)
        elif choice =='6':
            print("Closing the app.... ")
            break
        else:
            print('Invalid syntax..')

if __name__  == "__main__":
    main()


