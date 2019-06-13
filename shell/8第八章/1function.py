def greet_user(username="EveryOne"):
    print("Good morning " + username)

greet_user()
greet_user("lilei")

def display_message():
    print("display message")

def fav_book(book="thinking python"):
    print("you like " + book)

display_message()
fav_book("123")
fav_book()

def hello(name,messge):
    print("name=" + name + " message=" + messge)

hello("lilei","hello world")
hello(messge="hello",name="lily")