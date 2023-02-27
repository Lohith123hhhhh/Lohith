# to show working of string template class
from string import Template
t=Template('x is $x')
print(t.substitute({'x':1}))
# second example of string template class
x=Template('my name is $name')
print(x.substitute({'name':'lohith'}))
# third example of string template class
student=[('rohith',62),('dinesh',78),('firoz',51),('annirudh',91)]
y=Template('$name got $marks marks')
for i in student:
    print(y.substitute(name=i[0], marks=i[1]))
