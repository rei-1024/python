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