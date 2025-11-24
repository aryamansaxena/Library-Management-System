# Creating a book class which will act as the bases of all books data entered by the user
class Book:
    # using __init__ constructor along with several variables 
    def __init__(self, 
                book_id, 
                title, 
                author, 
                quantity, 
                price, 
                max_borrow_days):
        self.book_id=book_id#for id of the book
        self.title=title#for the the title 
        self.author=author#shows who wrote it 
        self.quantity=quantity#will tell the user how much are left or can he take them anymore 
        self.price=price#will be used to show the price
        self.max_borrow_days=max_borrow_days#a limit on how much can anyone take it 
        self.times_borrowed=0# and how many times someone is taking it, initially which i am setting it to 0

    def display(self):
        #Here i am defining the display function which will represent all of the information in the __init__ function.
        print("ID:", self.book_id, ", Title:", self.title, ", Author:", self.author,
              ", Quantity:", self.quantity, ", Price:", self.price,
              ", Max Borrow:", self.max_borrow_days, "days")

    def available(self):
        #available function is defined which checks if the quantity is more than 0 or not. If it is greater than 0 then it is suppposed to return the value
        return self.quantity>0

    def mquantity(self, n):
        #The main purpose of this function is to make changes in the quantity 
        self.quantity+=n

    def ibc(self):
        # this functions is needed to tell how may times a books is borrowd
        self.times_borrowed+=1
