#here i am importing datetime module and from it also importing timedelta
from datetime import datetime, timedelta
#here, i am making a class user which is needed to set the data of user who will enter the data 
class User:
    #Here i am using __init__ to define some data
    def __init__(self, uid, nm, rl='Member'):
        self.user_id = uid#i defined user id which is important
        self.name = nm#i defined name which is also important
        self.role = rl#i am now defining the role of the user which will be admin or member and the defualt role is i am selecting as member
        self.brw_bks = {} # this is a dictionary which i am defining to check which book user has 
    def borrow_book(self, bk, days):
        # now i am defining a function for borrwing books and it takes books and the number of days
        if self.role != 'Member':#if a person role is not a member 
            print(self.name,
                  "cannot borrow books")#then he cannot borrow books at all
            return
        if bk.available():#if the book is available then it can be only borrowed for some time. Not like that it can be borrowed forever
            if days>bk.max_borrow_days:
                print("Cannot borrow for more than",
                      bk.max_borrow_days,
                      "days")#here is the print line for it 
                return
            if bk.book_id in self.brw_bks:#if book line is already borrowed meaning already in brw_bks set then print that it is already borrowed.
                print(self.name, "already borrowed '",bk.title)
                return
            due_dt=datetime.now()+timedelta(days=days)#using datetime module here where we take current time and add with number of days entered by the user using delta function
            self.brw_bks[bk.book_id]=(bk,due_dt)#as the book has now been borrowed it is entered into user borrowed book dict.
            bk.mquantity(-1)# so now the quantity is also reduced to -1
            bk.ibc()#this function is needed to add the borrow count of the book
            #this print statement then showcases all the information
            print(self.name, 
                  "borrowed", 
                  bk.title, 
                  "for", 
                  days, 
                  "days, due on", 
                  due_dt.strftime('%Y-%m-%d'))
        else:
            #otherwise this print statement will be generated
            print("Book",bk.title,"not available")
    def return_book(self, bk):
        # here i am defining the return book function which also takes the name of the book
        if bk.book_id in self.brw_bks:#if condition to check whether the book was actually in the borrow books 
            del self.brw_bks[bk.book_id]#then it should delele it 
            bk.mquantity(1)#and then increase the quantity by 1 
            print(self.name,"returned",bk.title)# then it prints returned 
        else:
            print(self.name,"does not have", bk.title,"borrowed")#otherwise it will say borrowed cause it is not yet returned 
    def view_borrowed_books(self):
        # here i am defining a function to view all the borrowed books 
        if not self.brw_bks:# it shows that if the book is not in the borrowed books dictionary then print that the book has not been borrowed at all.
            print(self.name,"has no borrowed books")
            return
        print(self.name+" Borrowed Books:")#otherwise the book has been borrowed 
        now = datetime.now()#to get the current time 
        for bk, due_dt in self.brw_bks.values():# making a for loop which will check the book and it's due date in borrow books 
            days_left = (due_dt-now).days#calculates how much time is left by subtracting current time from deadline
            print("Title:", 
                  bk.title + 
                  ", Due in", 
                  days_left, 
                  "day on", 
                  due_dt.strftime('%Y-%m-%d'))#then print the output 
