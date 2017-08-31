import math
tryDict = {}
fi=open('bigrams_nonexperts.txt','r')
#fi=open('bigrams.txt','r')
alines=fi.readlines()
fi.close()
f2=open('output.txt','w')
for al in alines:
	vals=(al.rstrip('\r\n')).split(':')
    	freq=vals[1]
    	#freq=math.log(float(vals[1]),50)
    	if int(freq)>100:
    		words=vals[0].split(' ')
        	firstword=words[0]
        	secondword=words[1]
        	if (firstword!='amp') and (len(firstword)>1) and (len(secondword)>1):
        		try:
				tryDict[firstword][secondword]=freq
                	except:
				
                		tryDict[firstword]={}
                    		tryDict[firstword][secondword]=freq
fi=open('checkFlare.csv','w')
fi.write('id,value\n')
fi.write('flare,\n')
keys=tryDict.keys()
for key in keys:
        tempdict=tryDict[key]
        tdkeys=tempdict.keys()
        fi.write('flare.'+key+',\n')
        for tdk in tdkeys:
                fi.write('flare.'+key+'.'+tdk+','+str(tempdict[tdk])+'\n')
                fi.flush()
fi.close()

