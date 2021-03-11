# 创建一个程序类
class ChenXu:
    def __init__(self,name,itime,ctime,otime):
        self.name = name
        self.itime = itime
        self.ctime =ctime
        self.otime = otime

    def __str__(self):
        return("创建一个%s\n"
               "输入单位时间：%d\n"
               "CPU处理时间单位：%d\n"
               "输出单位时间：%d"%
               (self.name,self.itime,self.ctime,self.otime))

# 处理函数
def chuli(a,b,c,A,B,C):
    count = a
    if (b >= A):
        count += b
        if(B>=c):
            count += B+C
        else: count += c+C
    else:
        if(A+B <= b+c):
            count += (b+c+C)
        else: count += (A+B+C)
    return (count)

# 输入参数
t = ["输入","处理","输出","输入","处理","输出"]
s = []
for i in range(0,6):
    s.append(int(input("请输入%s单位时间:\n"% t[i])))

# 创建进程 A,B
A = ChenXu("进程A",s[0],s[1],s[2])
B = ChenXu("进程B",s[3],s[4],s[5])
print(A)
print(B)

# 求出时间
time = chuli(A.itime,A.ctime,A.otime,
             B.itime,B.ctime,B.otime)

print("%s和%s一共耗时%d个单位时间" % (A.name,B.name,time))