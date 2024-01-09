class Main: 
    def __init__(self) -> None: 
       age: str = input('Insert age: ')
       if (int(age) >= 18):
           print("Adult")
       else:
           print("Child")
       return None

if __name__ == "__main__":
    app = Main()