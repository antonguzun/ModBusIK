import time

def decode(arr: bytes):


    arr_rays = [0 for x in range(72)]
    k = 0
    for i in range(1,19):
        if(arr[i]&0b11000000 == 0b11000000):
            arr_rays[k] = 'n'
            k += 1
        if (arr[i]&0b00110000 == 0b00110000):
            arr_rays[k] = 'n'
            k += 1
        if (arr[i]&0b00001100 == 0b00001100):
            arr_rays[k] = 'n'
            k += 1
        if (arr[i]&0b00000011 == 0b00000011):
            arr_rays[k] = 'n'
            k += 1

    data = {'address': arr[0],
            'rays': arr_rays,
            'power': (arr[19]&0b01110000) >> 4,
            'configuration': arr[19]&0b00001111,
            'volt': (arr[20]/10 - 5),
            'rele': (arr[21]&0b10000000) >> 7,
            'time': time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
            }
    return data