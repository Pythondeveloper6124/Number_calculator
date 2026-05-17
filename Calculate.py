print("Enter exist If Your CalCulation Is Done")


try:
     i = "Make Exist iF the Work Is Done:"
     print(i)
     
     while i != "exist":
          
          #made signs and num1 and num2
          equation = input("write your number:")
          
          result = eval(equation)
          print(result)
     
     
except SyntaxError:
    print("Invalid symbol!")    

except IndentationError:
     print("IndentError")
     
             
except ValueError:
     print("Invalid words")     
     
except InterruptedError:
     print("User interruption")
