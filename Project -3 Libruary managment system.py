class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"There are several Book in our Library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-Book database updated .you can take book now")
        else:
            print(f"Bookis already taken by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book is succesfully added in list")

    def returnBook(self, book):
        self.booklist.pop()(book)


if __name__ == '__main__':
    manish = Library(['python', 'data structure',
                      'c programming', 'c++basic'], "codewithmanish")

    while(True):
        print(f"Welcome to the {manish.name} library.Enter your choice ")
        print("1. Display Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = int(input())

        if user_choice == 1:
            manish.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of book you want to land:")
            user = input("Enter your name:")
            manish.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            manish.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            manish.returnBook(book)
        else:
            print("not a valid option")

        print("press q to quit and c to continoue")
        user_choice2 = " "
        while(user_choice2 != "c"and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice == "c":
                continue
