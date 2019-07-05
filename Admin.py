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

def search():
    book_id = input("enter the id of book")
    with open("books_list.txt", 'r') as rf:
        text=rf.read().split()

        with open("issued_books.txt", 'r') as rf:
            issue=rf.read().split()
            if( book_id in text):
                if(book_id in issue):
                    print("Book is already issued")
                else:
                    if(book_id in text):
                        print("Book is there")
                    else:
                        def prints():
                            print("Book dosen't exist")

def all_books():
    with open("books_list.txt", 'r') as rf:
        for i in rf:
            print(i)

def exit():
    exit="f"

########################################### Main.py##################################

def main():
    exit="t"
    while(exit=="t"):
        print(""" ======LIBRARY MENU=======
                          1. Display all available books
                          2. Request a book
                          3. Return a book
                          4. Search a book
                          5. Add a book
                          6. Exit
                          """)

        choose=int(input("enter your choice"))
        if(choose==1):
            all_books()
        elif(choose==2):
            book_issue()
        elif(choose==3):
            return_book()
        elif(choose==4):
            search()
        elif(choose==5):
            add_books()
        else:
            sys.exit()
main()






