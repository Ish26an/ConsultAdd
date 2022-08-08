while True:
    try:
        n = input("Please enter four digit number: ")
        if len(n) > 4:
            raise ValueError
        # break
        else:
            print("Great, you successfully entered four digit number!")
            break
    except ValueError:
        print("Please try again ...")
