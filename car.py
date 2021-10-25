started = False
keyword = ""

while True:
    keyword = input("Type In Keyword: ").lower()
    if keyword == "stop":
        if started:
            started = False
            print("Car Has Been Stopped")
        else:
            print("Car Has Already Been Stopped")
    if keyword == "help":
        print("""
-- start = To Start The Car
-- stop = To Stop The Car
-- help = For Hints
-- quit = To End The Program
        """)
    if keyword == "start":
        if not started:
            started = True
            print("Car Has Been Started")
        else:
            print("Car Has Already Been Started")
    if keyword == "quit":
        break
    else:
        print("I Don't Understand That")
