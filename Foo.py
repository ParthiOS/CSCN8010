

class HelloWorld:
    def __init__(self):
        self.message = "Hello World"
        self.say_hello()

    def say_hello(self):
        print(self.message)


# Example usage:
if __name__ == "__main__":
    hello = HelloWorld()

