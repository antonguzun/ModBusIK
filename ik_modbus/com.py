import crc
import serial
import time

def form_req(adr: int):
    '''
    Form request frame kind: 0xXX(adress),0x00,0x00,0xXX(CRC low),0xXX(CRC high)
    :param adr: int
    :return: array lenght 5 bytes
    '''
    adr_byte = (adr).to_bytes(1, byteorder='big')
    req_val = adr_byte + b'\x00' + b'\x00'
    req_val = req_val + crc.crc16(req_val)
    return req_val

def com_session(adr: int):
    '''
    Make session with ine device
    TODO! EXCEPTION else answer of device is less than 24 bytes
    :param adr: int address of device
    :return: if CRC is ok: response from device - array of 24 bytes
            else: string 'ERROR CRC'
    '''
    time.sleep(0.05)                    #without this delay dont work
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM8'

    ser.open()
    while(not ser.writable()):
        a = 1
    ser.write(form_req(adr))

    while(not ser.in_waiting):
        pass
    s = ser.read(ser.in_waiting)

    crc_cal = crc.crc16(s[0:22])
    crc_real = s[len(s)-2:len(s)]
    if (crc_real == crc_cal):
        ser.close()
        return(s)
    else:
        ser.close()
        return('ERROR CRC')

def com_full_session(adr_arr: int):
    """
    like com_session, but work with array of addresses
    :param adr_arr: array of addresses
    :return: array of array
    """
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM8'

    ser.open()
    k = 0
    s = [0]*len(adr_arr)
    for i in adr_arr:
        while (not ser.writable()):
            a = 1
        ser.write(form_req(i))

        while (not ser.in_waiting):
            pass
        temp = ser.read(ser.in_waiting)
        time.sleep(0.05)

        crc_cal = crc.crc16(temp[0:22])
        crc_real = temp[len(temp) - 2:len(temp)]
        if (crc_real == crc_cal):
            s[k] = temp
        else:
            s[k] = 'ERROR CRC'
        k += 1
    ser.close()
    return s

def com_long_session(adr_arr, times = 10, loop = False):
    """
    TEST FUN
    :param adr_arr:
    :param times:
    :param loop:
    :return:
    """
    if (loop == True):
        while(1):
            pass
    else:
        for k in range(times):
            pass

#arr = [i for i in range(11,19)]
#print(time.clock())
#for i in range(8):
#    print(com_short_session(11))
#print(time.clock())
