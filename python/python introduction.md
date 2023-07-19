https://docs.python.org/3/library/functions.html (functions)

https://pythontutor.com/visualize.html#code=def%20fourcandles%28%29%3A%0A%20%20%20%20for%20i%20in%20range%284%29%3A%0A%20%20%20%20%20%20%20%20print%28%27candle%27%29%0A%0A%0A%0Aprint%28%27Here%20are%20your%20first%20four%20candles,%20for%20free!%27%29%0A%0Afourcandles%28%29%0A%0Amoreleons%20%3D%20%27y%27%0A%0Awhile%20moreleons%20%3D%3D%20%27y%27%3A%0A%20%20%20%20moreleons%20%3D%20input%28%27Would%20you%20like%20four%20more%20candles%3F%20y/n%3A%20%27%29%0A%20%20%20%20if%20moreleons%20%3D%3D%20%27y%27%3A%0A%20%20%20%20%20%20%20%20fourcandles%28%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false (python visualizor)


https://docs.python.org/3/py-modindex.html (module index)

https://pypi.org (package index)

def fourleons():
    leonlist = []
    for i in range(4):
        leonlist.append('Leon')
    return leonlist

print ('Here are your first four Leons')


returnlist = fourleons()

moreleons = 'y'

while moreleons == 'y':
    moreleons = input('Would you like more Leons? y/n: ')
if moreleons == 'y':
returnlist = fourleons()
print (returnlist)


-- IMPORTING

from [file name] import [function name]




