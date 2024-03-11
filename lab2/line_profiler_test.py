import time


@profile
def sleep_function():
    print('Sleep function start')
    time.sleep(5)
    print('Sleep function end')


if __name__ == '__main__':
    sleep_function()