import time
import com
import decoder as dec
from firebase import firebase

firebase = firebase.FirebaseApplication('https://iktest-61f5e.firebaseio.com/', None)

def test(arr):
    for i in arr:
        out = com.com_session(i)
        data = dec.decode(out)
        print(data)
        firebase.post('/ik', data, params='2')
        data = 0

arr = [i for i in range(11,19)]
#while(1):
print(time.clock())
test(arr)
print(time.clock())
