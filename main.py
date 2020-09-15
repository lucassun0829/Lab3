# Author: Lucas Sun lks5713@psu.edu
# Collaborator: Yousef Alzaabi yaa5136@psu.edu
# Collaborator: Maksim Zingman mfz5130@psu.edu
# Collaborator:
# Section: 2
# Breakout: 3
def sum_n(n): 
  if n>0:
    return n+sum_n(n-1)
  else:
    return 0

def print_n(s,n):
  if n>0:
    print(s)
    print_n(s,n-1)
  else:
    return  
    
def run():
  num = int(input("Enter an int: "))
  sum = sum_n(num)
  print("sum is "+str(sum)+".")
  s = input("Enter a string: ")
  print_n(s,num)

if __name__ =="__main__":
  run()
