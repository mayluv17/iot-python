def readTextFile(filename):
    try:
        with open(filename, 'r') as file:
            print(f"#### {filename} content ####")
            for line in file:
                print(line, end='')
            print(f"\n#### {filename} content ####")


    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def main():
    filename = input("Insert filename to read: ")
    readTextFile(filename)

if __name__ == "__main__":
    main()