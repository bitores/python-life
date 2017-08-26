#coding: UTF-8
import sys
import inspect as m

def foo():
    pass

class Cat(object):
    def __init__(self, name="kitty"):
        self.name=name
    def sayHi(self):
        print self.name,"says Hi!"


cat = Cat()

print Cat.sayHi # 使用类名访问实例方法时，方法是未绑定的(unbound)
print cat.sayHi # 使用实例访问实例方法时，方法是绑定的(bound)

print cat.name # 访问实例属性
#Cat.sayHi() # 调用实例方法
cat.sayHi() # 调用实例方法

print dir(cat)  # 获取实例的属性名，以列表形式返回
if hasattr(cat, 'name'): # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger') # 调用这个方法将给cat的名为name的值的属性赋值为tiger
    print getattr(cat, 'name') # 调用这个方法将返回obj中名为attr值的属性的值
    getattr(cat, 'sayHi')() # same as: cat.sayHi()

print isinstance(Cat, object)

# 模块。。。
print "#"*10
#__doc__: 文档字符串。如果模块没有文档，这个值是None。
#__name__: 始终是定义时的模块名；即使你使用import .. as 为它取了别名，或是赋值给了另一个变量名。
#__dict__: 包含了模块里可用的属性名-属性的字典；也就是可以使用模块名.属性名访问的对象。
#__file__: 包含了该模块的文件路径。需要注意的是内建的模块没有这个属性，访问它会抛出异常！ 


print m.__doc__.splitlines()[0] # Filename matching with shell patterns.
print m.__name__ # fnmatch
print m.__file__ # /usr/lib/python2.6/fnmatch.pyc
print m.__dict__.items()[0] # ('fnmatchcase', <function fnmatchcase="" at="" 0xb73deb54="">)</function>

print "#"*36

#__doc__: 文档字符串。如果类没有文档，这个值是None。
#__name__: 始终是定义时的类名。
#__dict__: 包含了类里可用的属性名-属性的字典；也就是可以使用类名.属性名访问的对象。
#__module__: 包含该类的定义的模块名；需要注意，是字符串形式的模块名而不是模块对象。
#__bases__: 直接父类对象的元组；但不包含继承树更上层的其他类，比如父类的父类。 

print Cat.__doc__ # None
print Cat.__name__ # Cat
print Cat.__module__ # __main__
print Cat.__bases__ # (<type ?object?="">,)
print Cat.__dict__ # {'__module__': '__main__', ...}</type>

#__dict__: 包含了可用的属性名-属性字典。
#__class__: 该实例的类对象。对于类Cat，cat.__class__ == Cat 为 True。

print cat.__dict__
print cat.__class__
print cat.__class__ == Cat # True

co = cat.sayHi.func_code
print co.co_argcount # 1 普通参数的总数，不包括*参数和**参数
print co.co_names # ('name',) 所有的参数名（包括*参数和**参数）和局部变量名的元组
print co.co_varnames # ('self',) 所有的局部变量名的元组
print co.co_filename # E:/pyworkspace/obj_attr.py 源代码所在的文件名
print co.co_flags & 0b100 # 0 


#inspect模块
    # is{module|class|function|method|builtin}(obj): 
    # 检查对象是否为模块、类、函数、方法、内建函数或方法。
    # isroutine(obj): 
    # 用于检查对象是否为函数、方法、内建函数或方法等等可调用类型。用这个方法会比多个is*()更方便，不过它的实现仍然是用了多个is*()。
im = cat.sayHi
if m.isroutine(im):
    im()

print "*"*12
print im.im_func #<function sayHi at 0x0000000002ADFF98>
print im.im_self # <__main__.Cat object at 0x0000000002A76320>
print im.im_class # <class '__main__.Cat'>

"""
getmembers(object[, predicate]):
这个方法是dir()的扩展版，它会将dir()找到的名字对应的属性一并返回，形如[(name, value), ...]。另外，predicate是一个方法的引用，如果指定，则应当接受value作为参数并返回一个布尔值，如果为False，相应的属性将不会返回。使用is*作为第二个参数可以过滤出指定类型的属性。
getmodule(object):
还在为第2节中的__module__属性只返回字符串而遗憾吗？这个方法一定可以满足你，它返回object的定义所在的模块对象。
get{file|sourcefile}(object):
获取object的定义所在的模块的文件名|源代码文件名（如果没有则返回None）。用于内建的对象（内建模块、类、函数、方法）上时会抛出TypeError异常。
get{source|sourcelines}(object):
获取object的定义的源代码，以字符串|字符串列表返回。代码无法访问时会抛出IOError异常。只能用于module/class/function/method/code/frame/traceack对象。
getargspec(func): 
仅用于方法，获取方法声明的参数，返回元组，分别是(普通参数名的列表, *参数名, **参数名, 默认值元组)。如果没有值，将是空列表和3个None。如果是2.6以上版本，将返回一个命名元组(Named Tuple)，即除了索引外还可以使用属性名访问元组中的元素。  
getargvalues(frame): 
仅用于栈帧，获取栈帧中保存的该次函数调用的参数值，返回元组，分别是(普通参数名的列表, *参数名, **参数名, 帧的locals())。如果是2.6以上版本，将返回一个命名元组(Named Tuple)，即除了索引外还可以使用属性名访问元组中的元素。
getcallargs(func[, *args][, **kwds]): 
返回使用args和kwds调用该方法时各参数对应的值的字典。这个方法仅在2.7版本中才有
getmro(cls): 
返回一个类型元组，查找类属性时按照这个元组中的顺序。如果是新式类，与cls.__mro__结果一样。但旧式类没有__mro__这个属性，直接使用这个属性会报异常，所以这个方法还是有它的价值的。
currentframe(): 
返回当前的栈帧对象。
"""

