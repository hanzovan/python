def counting(f):
    def wrapper():
        print("About to run the function")
        print("Will run the function in short time")
        f()
        print("Done running the function!")
    return wrapper

@counting
def hello():
    print("Hello, world!")

hello()