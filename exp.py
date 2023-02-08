import os
try:
    path = "C:\\Users\\ASC\\OneDrive\\Desktop\\aryasamajweb2" #change the drectory 
    os.chdir(path)
    
    os.system('cmd /k "python manage.py runserver" ') #runserver command
    ##code is working only runserver 
    paths = "C:\\Users\\ASC" #change the drectory 
    os.chdir(paths)
    print("now working directory" , os.getcwd())
    os.system('cmd /k "start msedge" ') #

except:
    print("could not execude command")
    

    
    
