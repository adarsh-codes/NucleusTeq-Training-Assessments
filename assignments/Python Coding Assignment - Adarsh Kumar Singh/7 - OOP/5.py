class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    def show_count(self):
        print(f"Number of instances created: {Counter.count}")

a = Counter()
b = Counter()

a.show_count()
