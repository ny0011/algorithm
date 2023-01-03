def check_uppercase(c):
  if c.isalpha() and str.upper(c) == c:
    return True
  print("No")
  exit()

def check_isnumber(S):
  if S.isnumeric():
      return True
  print("No")
  exit()

def check_length(S):
  if len(S) != 8:
    print("No")
    exit()
  return True
        
def check_number_range(num):
    if num < 100000 or num > 999999:
      print("No")
      exit() 
    return True    
    
S = input()
num = S[1:-1]

check_length(S)
check_uppercase(S[0])
check_uppercase(S[-1])
check_isnumber(num)
 
num = int(num)
check_number_range(num)
print("Yes")