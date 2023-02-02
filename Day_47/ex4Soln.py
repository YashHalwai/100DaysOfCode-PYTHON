# Exercise 4: Solutions and Shoutouts | Python Tutorial - Day #47

# https://www.youtube.com/watch?v=4lSQfOJKn7U&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=47


st = input("Enter message: ")

words = st.split(" ")
coding = input("1 for coding 0 for decoding:")
coding == True if (coding == "1") else False
print(coding)

if(coding):
    nwords = []
    for word in words:
        if(len(word) >= 3):   
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + st[1:] + st[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
            
    print(" ".join(nwords))        

else:
    nwords = []
    for word in words:
        if(len(word) >= 3):   
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
            
    print(" ".join(nwords))    
