# here i am importing datetime module which is a module in python
from datetime import datetime
#here i am creating a class called Reports
class Reports:
    #here i am creating a static method so this has nothing to do with instance and only to do with class
    @staticmethod
    def obr(users):#now i am making a obr functions which is taking user as input
        today= datetime.now()#using datetime function i am getting current time
        print("Overdue Books Report")#here, i am printing overdue book report as the title
        overduefound = False# and i am initially setting it's value as false
        for user in users:# then i am running a loop where user will iterate from each users data
            for book, duedate in user.brw_bks.values():#a nested loop so that the borrow books data of each user is passed to book and due date 
                if duedate < today:#condition where if duedate is less than today
                    daysoverdue = (today - duedate).days# then subtract the current day with the last deadline to return the book
                    # and then print how many days are left to print the book
                    print("User:", 
                          user.name, 
                          "Book:", 
                          book.title, 
                          "Days Overdue:",
                            daysoverdue)
                    overduefound=True# make it now true
        if not overduefound:#print this if overduefound is still false
            print("No overdue books")
    @staticmethod#create another static method
    def ubs(users):# define a ubs function which also takes user data as input
        print("User Borrow Summary:")# print this as the title
        for user in users:# run the loop 
            count=len(user.brw_bks)# here we are courting how many books are borrowed by the user
            print(user.name,
                  "has borrowed", 
                  count,
                  "book")#then print the output
