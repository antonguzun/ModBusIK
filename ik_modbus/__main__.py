import time
import com
import decoder as dec
#from firebase import firebase


def test(arr_adr):
    for i in arr_adr:
        out = com.com_session(i)           # 0.06 seconds
        data = dec.decode(out)
        print(data)
        #firebase.post('/ik', data, params='2')
        data = 0


#firebase = firebase.FirebaseApplication('https://iktest-61f5e.firebaseio.com/', None)

arr = [i for i in range(11, 19)]
print(time.clock())
test(arr)
print(time.clock())
