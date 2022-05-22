#implementasi hacker rank soal find digit ke dalam api sesuai dengan dc nomor 3 tanggal 20 dengan lebih dari satu request
from itertools import count
from flask import Flask,request

app = Flask(__name__)

def findDigits(n):
    # Write your code here
    count = 0
    lst = str(n)
    for x in lst:
        if int(x) != 0 and n % int(x) == 0:
            count += 1
    return count

@app.route('/digit', methods=['GET','POST'])
def find():
    req = request.get_json()['check']
    # n = req['check']
    lst1 = []
    for i in range(len(req)):
        gab = {
            "input": req[i],
            "output": str(findDigits(req[i]))
        }
        lst1.append(gab)
        # lst1.append(str(findDigits(req[i])))

    return {'result': lst1}
    
