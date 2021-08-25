# Raising an Exceptions
# You can raise exceptions in several ways by using the raise statement. The general syntax for the raise statement is as follows.
#
# Example; An exception can be a class or an object.
# Most of the exceptions that the Python core raises are classes, with an argument that is an instance of the class.
# Defining new exceptions is quite easy and can be done as follows −


def functionName1( level ):
   if level < 1:
      raise ("Invalid level!", level)
      # The code below to this would not be executed
      # if we raise the exception


# Note: In order to catch an exception, an "except" clause must refer to the same exception thrown either class object or simple string.
# For example, to capture above exception, we must write the except clause as follows −

def functionName( level ):

    try:
        if level < 1:
            raise ("Invalid level!", level)
    except Exception as e:
        if e.code == -2013:
            print("Exception handling here...")
    else:
       print("Rest of the code here...")


functionName(0)
