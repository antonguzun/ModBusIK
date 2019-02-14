from firebase import firebase


firebase = firebase.FirebaseApplication('https://iktest-61f5e.firebaseio.com/', None)


#result = firebase.post('/ik', data, params='2')
#print(result)
result = firebase.get('/ik', None )
print(result)
