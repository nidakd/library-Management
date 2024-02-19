class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
        print(f"{self.file} opened.")

    def __del__(self):
        self.file.close()
        print(f"{self.file} closed.")

    def list_books(self):
        self.file.seek(0)
        lines = self.file.readlines()
        print("List Books: ")
        for line in lines:
            book_list = line.strip().split(',')
            print(f"Book Name: {book_list[0]}, Author: {book_list[1]}")

    def add_book(self):
        book_title = input("Book Name: ")
        author = input("Author: ")
        release_date = input("Release Date: ")
        number_of_page = input("Number Of Page: ")
        book_info = f"{book_title},{author},{release_date},{number_of_page}\n"
        self.file.write(book_info)
        print(f"'{book_title}' added.")

    def remove_book(self):
        book_title_remove = input("Please enter the name of book to remove:")
        self.file.seek(0)
        lines = self.file.read().splitlines()

        index_remove = -1
        for i, line in enumerate(lines):
            if book_title_remove in line:
                index_remove = i
                break

        if index_remove != -1:
            del lines[index_remove]
            print(f"Book '{book_title_remove}' removed.")
        else:
            print(f"Book '{book_title_remove}' not found.")

        
        self.file.truncate(0)
        for line in lines:
            self.file.write(line + '\n')

lib = Library()

while True:
    print("\n****MENU****\n")
    print("1) List Books: ")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice:")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting the library system.")
        break
    else:
        print("Please enter list_books(1), add_book(2), remove_book(3, quit(q)")