def function():
  print("this is a function")
  a = 1 + 2
  print(a)

function()

def fun(a,b):
  c = a * b
  print("the c is",c)

fun(1,2)

#所有有默认值的参数，必须放到参数列表最后面
def sell_car(price,brand,length,height,color = "blue"):
  print("price is",price,
        "\ncolor is", color,
        "\nbrand is", brand,
        "\nlength is",length,
        "\nheight is",height)

sell_car(100,"benz",5100,"3t")

#在函数里定义全局变量用global，
#且一开始要给变量定义成None
a = None
def fun():
  global a
  a = 20
  return a + 100

print("a past is",a)
print(fun())
print("a now is",a)