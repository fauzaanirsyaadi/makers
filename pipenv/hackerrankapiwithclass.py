from flask import Flask
from flask import request
import base64

app = Flask(__name__)

class HackerrankSolver():
    def circularArrayRotation():
        res = request.headers.get("k")
        res = int(res)

        body = request.get_json()
        data = body["data"]
        query = body["query"]

        arr_baru = []
        for i in range(res):
            isi = data.pop(-1)
            data.insert(0, isi)
        for item in query:
            arr_baru.append(data[item])
        return {
            "result": arr_baru
        }
    def getTime(text):
        count = 0
        char = ord('A')

        for i in range(len(text)):
            beda = abs(ord(text[i]) - char)
            minValue = min(beda, 26 - beda)
            count = count + minValue
            char = ord(text[i])
        return {
            "time": int(count)
        }
    def minDiff():
        arr.sort()
        newArr=[]
        for i in range(len(arr)-1):
            newArr.append(arr[i]-arr[i+1])
        return abs(sum(newArr))
        # body = request.get_json()
        # arr = body['nilai']

        # arrBaru = sorted(arr)
        # for i in range(len(arrBaru)):
        #     a = abs(arrBaru[i] - arrBaru[i-1])
        # return {
        #     "a": int(a)
        # }
    
    def libraryFine():
        body = request.get_json()
        a = body['expected_date']
        b = body['actual_date']
        splitA = a.split("/")
        splitB = b.split("/")

        res = {}
        if int(splitA[2]) > int(splitB[2]):
            res["fine"] = 10000
        elif int(splitA[2]) < int(splitB[2]):
            res["fine"] = 0
        elif int(splitA[2]) == int(splitB[2]) and int(splitA[1]) < int(splitB[1]):
            res["fine"] = 0
        elif int(splitA[2]) == int(splitB[2]) and int(splitA[1]) == int(splitB[1]):
            if int(splitA[0]) < int(splitB[0]):
                res["fine"] = 0
            else:
                res["fine"] = 15 * (int(splitA[0]) - int(splitB[0]))
        elif int(splitA[2]) == int(splitB[2]):
            res["fine"] = 500 * (int(splitA[1]) - int(splitB[1]))
        return res

    def repeated_string(n):
        s = request.args.get("s")

        count = 0
        kali = n // len(s)
        for i in s:
            if i == 'a':
                count += 1
        count = count * kali

        for i in s[: n % len(s)]:
            if i == 'a':
                count += 1
        return {
            "frequency": count
        }
    def circularprint(self, text):
        text = text.upper()
        count = 0
        aVal = ord("A")
        non = ""

        for i in range(len(text)):
            if text[i].isalpha()==False:
                non += text[i]
            else:
                b=abs(ord(text[i])-aVal)
                minVal = min(b, 26-b)
                count +=minVal
                aVal=ord(text[i])
        if non !="":
            return 400, f"Expected alphabet, found non-alphabet characters: {non}"
        else:
            return 200, count
    def findFactor(self, number, find):
        number = int(number)
        find = int(find)
        lst =[1, number]
        i=2
        while i<=number//2:
            if number % i ==0:
                lst.append(i) 
            i+=1
        lst.sort()
        if find>len(lst):
            res=0
        else:
            res=lst[find-1]
        return res
    def getSort(self, arr):
        lst=[]
        for i in set(arr):
            lst.append([i, arr.count(i)])
        lst = sorted(lst, key=lambda x:(-x[1], x[0]))
        return lst

solve = HackerrankSolver

@app.route("/getTime/<text>", methods=["GET"])
def getTime(text):
    count = 0
    char = ord('A')

    for i in range(len(text)):
        beda = abs(ord(text[i]) - char)
        minValue = min(beda, 26 - beda)
        count = count + minValue
        char = ord(text[i])
    return {
        "time": int(count)
    }

@app.route("/minDiff", methods=["POST"])
def minDiff():
    # body = request.get_json()
    # arr = body['nilai']

    # arrBaru = sorted(arr)
    # for i in range(len(arrBaru)):
    #     a = abs(arrBaru[i] - arrBaru[i-1])
    # return {
    #     "a": int(a)
    # }
    body = request.get_json()
    arr = body["data"]
    res = solve.minDiff(arr)
    return{
        "minDiff":res
    }

@app.route("/libraryFine", methods=["POST"])
def libraryFine():
    body = request.get_json()
    a = body['expected_date']
    b = body['actual_date']
    splitA = a.split("/")
    splitB = b.split("/")

    res = {}
    if int(splitA[2]) > int(splitB[2]):
        res["fine"] = 10000
    elif int(splitA[2]) < int(splitB[2]):
        res["fine"] = 0
    elif int(splitA[2]) == int(splitB[2]) and int(splitA[1]) < int(splitB[1]):
        res["fine"] = 0
    elif int(splitA[2]) == int(splitB[2]) and int(splitA[1]) == int(splitB[1]):
        if int(splitA[0]) < int(splitB[0]):
            res["fine"] = 0
        else:
            res["fine"] = 15 * (int(splitA[0]) - int(splitB[0]))
    elif int(splitA[2]) == int(splitB[2]):
        res["fine"] = 500 * (int(splitA[1]) - int(splitB[1]))
    return res

@app.route("/repeated_string/nletter/<int:n>")
def repeated_string(n):
    s = request.args.get("s")

    count = 0
    kali = n // len(s)
    for i in s:
        if i == 'a':
            count += 1
    count = count * kali

    for i in s[: n % len(s)]:
        if i == 'a':
            count += 1
    return {
        "frequency": count
    }

@app.route("/password_check", methods=["PUT"])
def password_check():
    result = request.headers.get("Authorization")
    a = result.split(" ")

    user = base64.b64decode(a[-1]).decode('utf-8')
    b = user.split(":")

    if b[0] == "Andrew" and b[-1] == "NotaPassword":
        body = request.get_json()
        password = body["password"]

        special_characters = "!@#$%^&*()-+"
        count = [0, 0, 0, 0]
        n = len(password)
        for char in password:
            if char.isdigit():
                count[0] = 1
            elif char.isupper():
                count[1] = 1
            elif char.islower():
                count[2] = 1
            elif char in special_characters:
                count[3] = 1
        res = max(6 - n, 4 - sum(count))

        return {
            "character_to_add ": res
        }

    else:
        return "Invalid User or Password", 401

@app.route("/marsExploration")
def marsExploration():
    
    s = request.args.get("s")

    word = "SOS"
    diff = 0

    for i in range(0, len(s), 3):
        for j, c in enumerate(word):
            if c != s[i+j]:
                diff += 1
    return {
        "corrupted": diff
    }

@app.route("/saveThePrisoner/prisoners/<int:n>/candy/<int:m>", methods=["POST"])
def saveThePrisoner(n, m):
    s = request.args.get("s", "1")
    s = int(s)

    total = (s + m - 1) % n
    return {
        "warn": total
    }

@app.route("/circular_array")
def circularArrayRotation():
    res = request.headers.get("k")
    res = int(res)

    body = request.get_json()
    data = body["data"]
    query = body["query"]

    arr_baru = []
    for i in range(res):
        isi = data.pop(-1)
        data.insert(0, isi)
    for item in query:
        arr_baru.append(data[item])
    return {
        "result": arr_baru
    }

@app.route("/circularprint/<text>", methods = ["GET", "POST", "PUT"])
def circularprint(text):

    code, res = solve.circularprint(text)
    return{
        "time" : res
    },code #400

@app.route("/sortSummary", methods=["GET", "POST", "PUT"])
def getSort():
    body = request.get_json()
    arr = body["data"]
    res = solve.getSort(arr)
    return {
        "getSort":res
    }



