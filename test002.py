#1. use ","
print ("Hello bro",456,"HI john...",True,20+35,"Hey John...")
#2. ues "+" (only str)
print ("Hello bro"+("456")+"HI john..."+"True"+("20+35")+"Hey John...")
print ("Hello bro"+str(456)+"HI john..."+str(True)+str(20+35)+"Hey John...")
print ("Hello bro "+str(456)+" HI john... "+str(True)+' '+str(20+35)+" Hey John... ")
#3. ues ".format"
print ("Hello bro {} HI john... {} {} Hey John...".format(456,True,20+35))
print ("Hello bro {0} HI john... {1} {2} Hey John...".format(456,True,20+35))   #idex number
print ("Hello bro {1} HI john... {2} {0} Hey John...".format(456,True,20+35))   #idex number
#4. use f-string
print (f"Hello bro {456} HI john... {True} {20+35} Hey John...")
print (F"Hello bro {456} HI john... {True} {20+35} Hey John...")
#5. use modulas oprator (%) -> %d, %f, %c, %s, %i (False[0],True[1]), ....
print ("Hello bro %d Hi john... %s %d Hey John..."%(456,True,20+35))