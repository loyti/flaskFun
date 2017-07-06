words = "It's thanksgiving day. It's my birthday,too!"
print words.replace("day", "-month")

a = [2,54,-2,7,12,98]
b = max(a)
c = min(a)
print b
print c
print min(a) + max(a)

d = ["hello",2,54,-2,7,12,98,"world"]
e = []
e.append(d[0])
e.append(d[len(d)-1])
print e

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y = x[:len(x)/2] 
z = x[len(x)/2:]
print "1st List", y
print "2nd List", z
z.insert(0,y)
print z
