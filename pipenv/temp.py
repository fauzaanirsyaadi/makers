# my_set = set([1, 1, 2, 3])
# # print(my_set)

# my_set = {1, 2.0, "Python", (3, 4, 5)}
# print(my_set)
import requests
params = {
    "per_page" : "50"
}

r = requests.get('https://api.github.com/repos/JuliaLang/julia/issues?page=1?per_page=50',
                 auth=('fauzaanirsyaadi', '17dc14e4b5169855859d4e3338ee0df18b4c1e86'), params=params)
# r.headers['17dc14e4b5169855859d4e3338ee0df18b4c1e86']
result = r.json()
r.text
# print(r.status_code)
# print(r.json())
isi=[]
for i in result:
    # print(i["user"]["login"])
    isi.append(i["user"]["login"])
    # print(result["user"])
setelah_set = set(isi)
print(setelah_set)