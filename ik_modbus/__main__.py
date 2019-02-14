import time
import com
from decoder import decode
from firebase import firebase

firebase = firebase.FirebaseApplication('https://iktest-61f5e.firebaseio.com/', None)

def test():
    for i in range(11,19):

        out = com.com_session(i)
        data = decode(out)
        print(data)
        firebase.post('/ik', data, params='2')
        data = 0

while(1):
    test()
