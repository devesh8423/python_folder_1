#BLL
def func1(a,b):
    return a+b

#PLL
if(__name__=="__main__"): # ye likhne ka seedha matlb hai isi file me run kroge to variable __name__ ka naeme __main__ hoga 
                            # aur ye dusre file me run hoga to __name__ usi file ka name hoga na ki __main__ ye kewal usi file me hota hai
    print("Devesh")
    print("Welcome")
    print(func1(9,3))


    
# c=func1(1,2)
# print(c)

'''Here __name__ is a variable, which is created automatically by
python interpreter. whenever we are running a program then __name__ of that program becomes __main_-
but when we access aprogram  (module)from another program 
then __name__ of that program(module) becomes its actual name '''
