#to calculate length of string
mystr = "hello world"
print(len(mystr))


a="hello"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(a, str(b))


mystr="hello"
if len(mystr) > 1:
    print(mystr[:2]+mystr[-2:])
else:
    print("empty string")


mystr="hello"
x = mystr.replace( "e" , "$")
print(x)


str1 ="hello"
str2="world"
str3 = str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]
print(str3)


a ="fast"
if len(a) < 3:
    x = a
elif a[-3:] == "ing":
    x = a + "ly"
else:
    x = a + "ing"
print (x)

mystr="welcome"
n =3
x= mystr[:n-1] + mystr[n:]
print(x)


mystr="hello"
x= mystr[-1] + mystr[1:-1] + mystr[0]
print(x)
########################################################################################################################
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {1, 2, 3}

set3 = set1.intersection(set2)

if set3 == set2:
 print("set2:",set2,"is a subset of set1:",set1)
else:
 print("set2 not a subset of set1")


a="hello"
b=""
for i in range(len(a)):
    if (i%2 == 0):
        b+= a[i]
print(b)



mystr= input("enter any word :  ")

print(mystr.upper())
print(mystr.lower())



string="This is a sample Python program, Welcome to World Of Python Programming!"
word="Python"
list=[]
wordCount=0
list=string.split(" ")
for i in range(0,len(list)):
      if(word==list[i]):
            wordCount=wordCount+1
print("Number of occurrences found in the string:")
print(wordCount)


items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))


def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))


text ="[['']]"
text ="{[(<<>>)]}"
text ="< />"
text ="<< />>"
middle = "python"
index = (len(text))//2
print (text[:index] + middle + text[index:])


def insert_end(str):
    sub_str = str[-2:]
    return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises')


def first_three(str):
    return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))


str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])


def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('python'))


def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]:
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))


lis = "\n SUVIDHA \n"
string = lis.strip()
print(string)


string = "suvidha"
print(string.startswith("suv"))