class sample:
    def __init__(self):
        self.a = 25
        self.__b = 100


def main():
    obj = sample()
    print(obj.a)
    print(obj._sample__b)

if __name__ == "__main__":
    main()