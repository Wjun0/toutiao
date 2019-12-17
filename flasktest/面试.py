
for i in range(4):
    i +=1
    if 3 == ((i !=1) + (i==3) + (i==4) + (i !=4)):
        print(chr(96 + i) + '是小偷')


class Sample(object):
    def start(self,n):
        try:
            n = int(n)
        except:
            return '请输入整数'
        if n == 1:
            return 1
        elif n ==2:
            return 2
        else:
            return self.start(n-1) + self.start(n-2)

a = Sample()
print(a.start(5))



def fibo(n):
  assert n >= 0, "n > 0"
  if n <= 1:
    return n
  return fibo(n-1) + fibo(n-2)

def result(x):
    lis = []
    for i in range(20):
        lis.append(fibo(i))
        if max(lis) > x:
            return lis
    return lis

print(result(232))


