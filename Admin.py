from datetime import datetime
import sys
with open("books_list.txt",'a+') as f:

    def add_books():
        number=int(input("enter the books to add to library"))
        for i in range(number):
            book_id=(input("enter the book id"))
            book_name=input("enter the book name")
            f.write("\n"),f.write(book_id),f.write(" ")
            f.write(book_name),f.write("\n")


    # add_books()
    def all_books():
        with open("books_list.txt", 'r') as f:
            for i in f:
                print(i,end="")


    def book_issue():
        with open("books_list.txt", 'r') as f:
            text = f.read().strip()
            book_issue = int(input("enter the books you want to issue"))
            for i in range(book_issue):
                book_id=input("enter the id of book")
                with open("books_list.txt",'r') as rf:

                    if(book_id in text):
                        with open("issued_books.txt","w") as wf:
                            wf.write("\n")
                            wf.write(book_id),wf.write(" ")
                            wf.write('%s' %datetime.now())
                            wf.write("\n")
                            print("Book has been isued")
                    else:
                        print("Book dosen't exist")

# book_issue()
with open("issued_books.txt",'r') as rf:
    def return_book():
        book_return = int(input("enter the books you want to return"))
        for i in range(book_return):
            book_id = input("enter the id of book")
            with open("issued_books.txt", 'r') as rf:
                text = rf.read().strip().split()
            with open("issued_books.txt", "w") as wf:
                for i in text:
                    if(i!=book_id):
                        wf.write("\n"), wf.write(i)
                        wf.write("\n")

# return_book()




