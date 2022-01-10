user = {"username":"password"}
# truy cap 1 account
print(user["username"])

task = {"username":{0:["task","address","start","end", False]}}
# truy cap task name
print(task ["username"][0][3])

f = open('data/user.dat','rb+')
f.truncate()
