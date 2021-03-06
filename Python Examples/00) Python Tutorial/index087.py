# Python Try Except


# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.






# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

# Example
# The try block will generate an exception, because x is not defined:



print(" ")


try:
  print(x)
except:
  print("An exception occurred")













# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

# Example
# Print one message if the try block raises a NameError and another for other errors:

#The try block will generate a NameError, because x is not defined:


print(" ")


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
  
  
  
  
  
  
  
  
  
  
# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:

# Example
# In this example, the try block does not generate any error:


#The try block does not raise any errors, so the else block is executed:

print(" ")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")











# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.

#The finally block gets executed no matter if the try block raises any errors or not:

print(" ")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
  
  
  
  
  
  



# This can be useful to close objects and clean up resources:

# Example
# Try to open and write to a file that is not writable:


# The try block will raise an error when trying to write to a read-only file:

# The program can continue, without leaving the file object open.


print(" ")


try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
  
  print(" ")