#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ColorGame():
    color = ""
    while color != "done":
        color = input("Give your favorite color? When finished, write 'done'")
        if color != "done":
            print("That's a cool color!")
        else:
            print("Goodbye")
            

