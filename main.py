# remember to fork this and push to github

# f = open('test.txt', 'r')
# print(f.readlines())
# f.close()

# with open('test.txt', 'r') as f:
#   f_contents = f.readlines()
#   print(f_contents, end='')

# employee_file = open("employees.txt", "r")

# print(employee_file.readline()[1])
# print(employee_file.readline())
# print(employee_file.readline())

# employee_file = open("employees.txt", "r")
# for employee in employee_file.readlines():
#   print(employee)
# employee_file.close()

# employee_file.close()

# employee_file = open("employees.txt", "a")

# employee_file.write("Toby - Human Resources")

# employee_file.write("/nKelly - Customer Service")


# employee_file.close()

# employee_file = open("employees.txt", "w")

# employee_file.write("/nKelly - Customer Service")

# employee_file.close()

# employee_file = open("omindex.html", "w")

# employee_file.write("<p>This is HTML</p>")

# employee_file.close()

with open('readme.txt','w') as f:
  f.write('readme')

#This overwrites the original content
with open('readme.txt','w') as f:
  f.write("I don't care")

#This appends to the original content
with open('readme.txt','a') as f:
  f.write("I don't care I don't care I don't care")
  
