@profile
def data_append_function():
    print('Data append function start')
    data = []
    for i in range(100000):
        data_in = i // 2
        data.append(data_in)

    print('Data append function end')
    return data


if __name__ == '__main__':
    _ = data_append_function()