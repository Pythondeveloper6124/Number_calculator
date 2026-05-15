print("Enter Exist If Your CalCulation Is Done")


try:
     i = input("Make Exist iF the Work Is Done:")
     print(i)
     
     while i != "Exist":
          
          #made signs and num1 and num2
          choice = input("Choose The Sign(*/+/-/=/÷/×/**/):")
          num1 = int(input("Enter The Number:"))
          num2 = int(input("Enter The Second Number:"))
            
         
    
  
     match choice:
               case "+":
                    ans3 (int(num1)+int(num2))
                    print(ans3)
               
               case "-":
                    ans2 = (int(num1)-int(num2))
                    print(ans2)
     
     
               case "**":
                      ans = (int(num1)**int(num2))
                      print(ans)
               
                    
               
               
               case "/":
                    print(int(num1)/int(num2))
               
               
       
               
     
     
     
except IndentationError:
     print("IndentError")
     
             
except ValueError:
     print("Invalid words")     
     
except InterruptedError:
     pass  
