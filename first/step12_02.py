#-*- encoding: utf-8 -*-

#储存与取储存

import cPickle as p
#import Pickle as p

shoplistfile = 'shoplist.data' #define the name of the file where we will store the object

shoplist = ['apple','mango','carrot']

#write to the file
f = file(shoplistfile,'w')
p.dump(shoplist,f) #dump the object to a file 储存
f.close()

del shoplist #remove the shoplist

#read back from the storage
f = file(shoplistfile)
storelist = p.load(f) #取储存
print storelist
