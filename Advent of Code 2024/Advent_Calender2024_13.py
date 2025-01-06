mm = open("Input2024_13.txt","rt").read().split("\n\n") # claw machines
#mm = open("Test.txt","rt").read().split("\n\n") # claw machines

def getcoords(s):
  s = s.replace("=","").replace("+","").replace(",","")
  x = s.find("X")
  b = s.find(" ",x)
  y = s.find("Y",b)
  return int(s[x+1:b]),int(s[y+1:])

def solve(m,add=0):
  (ax,ay),(bx,by),(px,py) = map(getcoords,m.splitlines())
  px += add; py += add
  t1,t2 = bx*py-by*px,bx*ay-by*ax
  if t1%t2: return 0
  ak = t1//t2
  t3 = (px-ax*ak)
  if t3%bx: return 0
  bk = t3//bx
  return ak*3+bk

print(sum(solve(m) for m in mm))
print(sum(solve(m,10000000000000) for m in mm))