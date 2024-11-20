#coding=utf-8    #中文声明注释，可以更改为gbk等，将此文件用记事本打开时，另存为，即可发现文档编码方式为此处所记录，必须放在第一行

'''
多行注释
牛逼
'''

a = aa = 2
b = 3
print(a * b,a)#不换行输出
print('这是你')

print(chr(98))#ASCⅡ表输出
print(ord('六'))#中文Unicode码输出
print(chr(20845))

file1=open('note.txt','w')#w为write 文件处理
print('厉害',file=file1)
file1.close()

#print(value=,sep=' ',end='/n',file=)为print函数
print('厉害',666,sep='&',end=' ')#sep为间隔符
print(123)

#input内容为字符串
num=input('输入num吧:')
print('输出吧:'+num)#只能连接字符串
num=int(num)
print(num)

#class,def等采用严格的4空格缩进保证逻辑

#and,as,assert,break,class,continue,def,del,elif,else,except,finally,for,from,False,global,if,import,in,ij,lambda,nonlocal,not,None,or,pass,raise,
#return,try,True,while,with,yield,await,async为保留字，不能被设为变量，严格区分大小写
import keyword#导入内置函数
print(len(keyword.kwlist))#输出多少保留字

'''
标识符命名规则
1.字符，下划线，数字，中文，第一个字符不能是数字，不建议中文和下划线，后者如com_ha是“包”
2.类：MyClass,即Pascal风格，而_MyClass为模块内部的类
3.常量全大写，可以用下划线
4._开头的模块变量或函数是受保护的，用“from ... import”从模块中导入时不能被导入
5.__开头的实例变量或方法是类私有的
6.__init__()表示初始化函数，这种开头结尾是python专有标识
'''

print(type(a))#查看数据类型
print(id(a),id(aa))#查看内存位置

#0b101,0B101 二进制bin    0o101,0O101 八进制oct      0x10A,0X10A 十六进制hex
# ord（）将字符转化成对应的整数值，对应chr，利用Unicode表

x=1+2j#虚数的引入
print(round(0.1+0.2,1),0.1+0.2,1.9E2,x.imag,x.real)  #浮点型，保留几位小数(尾数不确定)，科学计数法

'''
字符串转义字符
\n换行 \t水平制表位，用于横向跳到下一制表位,一个制表位占四个字符 \"双引号 \'单引号 \\一个反斜杠
在转义字符前转义使字符失效，r或R
'''
print('''
爽
\"真爽\"
haha\tha
hahah\tha
hahaha\tha
hahahah\tha
hahahaha\tha''')#输出多行字符 三引号

'''
字符串索引，有正向和反向
-3 -2 -1
a  b  c
0  1  2
'''
s='haha' #a,b,c,d='haha'字符串分解赋值
ss='heihei'
print(s[1],'hei'[1],s[1:3])#结果不包含第三位
print(s+ss,s in ss,s*2)#连接，布尔判断是否包含,true为1,可直接转化为int，复制

print(bool(1),bool(0.0),bool('ha'),bool(None),bool(False))#0，空，False，None为false

'''
数据类型转化
浮点转整型 保留整数 -3.9到-3   相反，到一位小数
字符串转整数，100可以，10a不可以，3.1不可以
字符串转浮点，2a.1不可以
'''

print(eval('1+1'))#将字符串转化为浮点或整型
m='he'
print(eval('m'))
#print(eval('he'))报错，没有he这个变量

'''
//整除 %取余 **幂运算 除法得浮点型  幂运算最高，加减最低，其余中间
简略赋值也可使用：x=y x+=y x-=y x*=y x/=y x**=y x//=y x%=y
系列解包赋值 a,b=1,2 可应用于交换两变量的值
比较赋值，结果为布尔值
逻辑运算符 a and b逻辑与，从左到右，只有T and T为T   a or b逻辑或，从左到右，只有F or F为F  not a逻辑非，从右到左，取反  结果为布尔值
位运算 按位与&，类比逻辑与，只有1&1=1  按位或|，类比逻辑或，只有0|0=0 按位异或^，不同为1 按位取反~，~n=-（n+1） <<左移位（右），如2<<2=2*2*2=8，8>>2=8/2/2=2
  优先级比较：幂运算>取反，正负号>乘除取余整除>加减>移位>按位与>按位异或>按位或>比较>赋值
注意使用逻辑运算符时两边是表达式，不能出现a==1 or 2的情况
'''

if not num%2: #if语句，结果为布尔,即if true 则···
    print('偶数')
if input('空吗？'):
    print('不空')
if eval(input('来个布尔')) and 1==1:#and,or表示复合条件
    print('真')
elif 1==2:
    print(6)
else:
    print('假')
print('heihei' if not num%2 else 'kuku')#条件语句的简化

grade=input('A,B')#模式匹配 match case 函数
match grade:
    case 'A':
        print('great')
    case 'B':
        print('not bad')

sum=0
for i in range(1,11):#for-in循环，range[n,m)的整数
    sum+=i
    if 1!=1:break #也不执行else内容   #continue也可用,直接到下一次循环
else:#for-else 遍历的拓展
    print(sum)
for i in 'hello':#还可是文件，组合数据等
    print(i)

w=6#初始化变量   while-else语句亦适用
while w==6:#条件判断
    print(6)#语句块
    w=input('6吗？')#改变变量     #四步

print(str(a)+str(b))#+号连接字符串，str（）作形式转换

import random#产生随机数
rand=random.randint(1,100)

#序列切片
st='helloworld'
st1=st[0:6:1]#开头，结尾（不包含），步长
st1=st[2:]#省略结尾和步长，默认为最后和一，可以把两个冒号合并成一个
st1=st[::-1]#步长为-1，逆序输出,不能讲两个冒号合并为一个

#字符串内置函数,元组也可以使用
print(st1 in st,st1 not in st,len(st),max(st),min(st),st.index('o'),st.count('o'))#前两个返回布尔值，判断前面是否在或不在后面内部，后两个为打点调用，位置和出现次数

#列表的操作   在列表中，00被视作0
l=[1,2.2,'ha']#可变数据类型
print(l)
l=list('haha')
l=list(range(1,10,2))
del l#列表多出来一个删除操作，结果为l无定义报错
l=['a','b','c','d']#三种遍历方式
for i in l:
    print(i)
for i in range(0,len(l)):
    print(l[i])
for i,j in enumerate(l,start=1):#start可省略，全不写时start默认为0，i为序号，不是索引,初始值为start
    print(i,j)

#列表的特有操作，不改变列表内存地址
l.append('la')#增加至末尾
l.insert(1,'hu')#插入到某个序号之后
l.remove('hu')#删除
print(l.pop(1))#根据索引！将元素取出再删除
l.clear()#清除所有元素
l=['a','b','c']
l.reverse()#列表反向   只需这样使用即可，若在print内部，因为这只是一个操作，没有返回值，所以结果是None
l1=l.copy()#列表的复制，产生一个新列表
l[1]='lala'#列表元素修改，根据索引

'''
列表的排序，两种方法
l.sort(key=None,reverse=False) 前面是排序规则，后面是排序方式，默认升序
sorted(?,key=None,reverse=False) ?处为排序对象
字符串排序时，根据ASCⅡ码排序，升序时先大写后小写
key=str.lower表示无视大小写
类型不相同时会报错无法排序
'''
print(l)
l.sort()
print(l)

#列表的生成
l.clear()
l=[i*2 for i in range(10) if i%3]
print(l)

#二维列表的生成
l=[
    ['1,1','1,2'],#不要忘记逗号
    ['2,1','2,2']
]
l=[[j for j in range(2)] for i in range(2)]

#二维列表的遍历
for i in l:#i为第几行
    for j in i:#j为该行中的第几个元素
        print(j,end='\t')
    print()

#元组的创建，遍历，删除  为不可变数据类型，只能用索引，只有一个元素时逗号不能省略    访问速度快，可以当作字典的键，这是不同于列表的地方
t=('hello',[1,2])
t=tuple('hello')
t=tuple([1,2])
t=(10,)#(10)此时t类型为整型
del t
t=('hello','world','helloworld')#元组三种遍历方式
print(t[0],t[0:3:2])#支持切片操作
for i in t:
    print(i)
for i in range(1,len(t)):
    print(t[i])
for i,j in enumerate(t):#同列表
    print(i,j)
#元组生成器
t=(i for i in range(1,4))#此时无法查看内容
print(t)
t=tuple(t)#此时可以查看内容
print(t)
t=(i for i in range(1,4))#还有另一种不用将生成器转化为元组的方法
print(t.__next__())#按照索引将元素取出，类似pop（）

#字典   |可实现字典合并
d={1:'hei',2:'ha',2:'hai'}#键不变，值覆盖
d=dict(one=1,two=2)#左是键，右是值
#生成法
l1=[1,2]
l2=['li','hai',666]
z=zip(l1,l2)
'''此时结果为生成器，有两种处理方法
1.list(z)转为列表
2.dict(z)转为字典
这两种只能出现一种，因为任何一种操作都会将元素从生成器中取出，类似pop()
max,min,len,del都可使用
字典的键是无序的，有序是编译器的问题
d=d1等字典赋值时，二者占用同样的内存空间，一个改，另一个跟着改
键必须存储不可变数据类型
'''
z=dict(z)
print(z[1],z.get(2,'不存在'))#key不存在时，前者报错，后者返回None，逗号后面是返回的默认值
#字典的遍历
for i in z.items():#输出键值对
    pass
for i,j in z.items():#前面是键
    pass
#字典的特殊操作
z[3]='liu'#直接赋值
k=z.keys()#获取字典中所有的键，值同理
print(k)#此时得到的是一个对象，可以将它取出转为字典或元组，list(),tuple()
l=z.items()#与上一行同理
print(z.pop(3))#同列表，也遵循get的规则，可设定默认值
print(z.popitem())#随机删除一个键值对
z.clear()#清空
bool(z)#此时为False，因为为空字典                                   任何一个对象都对应一个布尔值
#两种字典生成式
z={i:i*2 for i in range(1,4)}
z={i:j for i,j in zip(l1,l2)}

#集合   与数学类似，是可变数据类型，只能存储不可变数据,无序存储
s={1,2,3}
s=set('halo')#[1,2,3],range(4,6)也可放入set
s={}#此时创建空字典
s=set()#此时创建空集合
#max,min,len,del可以使用
#集合操作符:&|-^交并差补，其中补集是交集的补集
s.add(4)
s.remove(4)
s.clear()#添加，删除，清空
for i in s:
    pass
for i,j in enumerate(s):
    pass
s={i for i in range(1,4) if i==i}#生成是与两种遍历

#结构模式匹配，字典，元组，列表
m=eval(input('试试:'))
match m:
    case {6:6}:
        print('字典')
    case _:
        print('失败')

#同步迭代
z=zip(l1,l2)#必须以生成器形式
for i,j in z:
    match i,j:
        case 1,'li':
            print(6)
        case 2,'hai':
            print(66)
