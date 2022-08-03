import datetime
from os.path import exists
if not exists('work.txt'):
    with open('work.txt','w') as file:
        file.write(f"|{'Function name':<20}|{'Worked time':<30}|{'Arguments as dictionary':<30}|{'Function result':<20}|\n")
def logger(f):
    def wrapper(*args,**kwargs):
        try:
            result=f(*args,**kwargs)
        except ZeroDivisionError:
            result='Zerodivision'
        except TypeError:
            result='Type Error'
        except ValueError:
            result='Value Error'
        except:
            result='Error'
        with open('work.txt','a+') as file:
            if args and kwargs:
                file.write(f"|{f.__name__:<20}|{str(datetime.datetime.today()):<30}|{str(args):<20}|{str(kwargs):<20}|{str(result):<20}|\n")
            elif args:
                file.write(f"|{f.__name__:<20}|{str(datetime.datetime.today()):<30}|{str(args):<20}|{str():<20}|{str(result):<20}|\n")
            else:
                file.write(f"|{f.__name__:<20}|{str(datetime.datetime.today()):<30}|{str():<20}|{str(kwargs):<20}|{str(result):<20}|\n")
    return wrapper

@logger
def sum(a,b):
    return a+b
@logger
def divide(a,b):
    return a/b
sum(1,2)
divide(a=4,b=2)
divide(10,0)
sum(1,'a')