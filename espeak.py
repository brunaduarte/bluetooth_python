import os  

name1 = "Hello, Hello Bruna"
name2 = "Hello, Hello Button"

def say(name):
 os.system('espeak -ven+f2 -k5 -s150 "{}"'.format(name))
 
say(name2)
