# Exercise 7 - Clear the Clutter | Python Tutorial - Day #68

# os.rename

import os
def func(path,extention):
  a=os.listdir(path)
  new_name=1
  for i in a:
    if i.endswith("."+extention):
      os.rename(path+"/"+i,path+"/"+str(new_name)+"."+extention)
      new_name+=1

func("Files","pdf")