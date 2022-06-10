import time

def say_after(delay, what):
    time.sleep(delay)
    print(what)


def main():
    print(f"started at {time.strftime ('%X')}")

    say_after(1, 'hello')
    say_after(2, 'world')

    print(f"finished at {time.strftime ('%X')}")

main()