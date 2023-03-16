# 13).Explain Exception handling? What is an Error in Python ? 

"""

Exception Handling :

-> Exceptions can be unexpected or in some cases, a developer might expect some disruption in the code flow due to an exception that might come up in a specific scenario. Either way, it needs to be handled.
-> Python just like any other programming language provides us with a provision to handle exceptions. And that is by try & except block. Try block allows us to write the code that is prone to exceptions or errors. If any exception occurs inside the try block, the except block is triggered, in which you can handle the exception as now the code will not go into a halt state but the control will flow into the except block where it can be manually handled.
-> Any critical code block can be written inside a try clause. Once the expected or unexpected exception is raised inside this try, it can be handled inside the except clause (This ‘except’ clause is triggered when an exception is raised inside ‘try’), as this except block detects any exception raised in the try block. By default, except detects all types of exceptions, as all the built-in exceptions in python are inherited from common class Exception.

Error :

-> Error is an illegal operation performed by the user which results in abnormal working of the program. Programming errors often remain undetected until the program is compiled or executed. Some of the errors inhibit the program from getting compiled or executed.

"""