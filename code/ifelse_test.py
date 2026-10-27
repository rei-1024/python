x,y,z = 1,2,3
if x < y:
  print("y,nb")

if x <= y:
  print("x is less or equal than y")

if x == y:
  print("x is  equal to y")

#else也要加冒号 if和else在同一位置
if x != y:
  print("x is not equal to y")
else:
  print("x is equal to y")

#elif == else if
#满足一个条件会直接跳出if，执行后面语句
if x == y:
  print("x is equal to y")
elif x > y:
  print("x is bigger")
else:
  print("x is smaller")