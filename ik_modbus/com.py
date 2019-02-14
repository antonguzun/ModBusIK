import crc
import serial
import time

def form_req(adr: int):
    adr_byte = (adr).to_bytes(1, byteorder='big')
    req_val = adr_byte + b'\x00' + b'\x00'
    req_val = req_val + crc.crc16(req_val)
    return req_val

def com_session(adr: int):
    time.sleep(0.05)
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
        print('ERROR CRC')
        return('ERROR CRC')


#for i in range(30):
#    print(com_session(11))

