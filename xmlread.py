import xml.dom.minidom as minidom
doc = minidom.parse('source.xml')
f1 = open('test1.txt','w+')
#f2 = open('test2.txt','w+')
#f3 = open('test3.txt','w+')
#f4 = open('test4.txt','w+')
#f5 = open('test5.txt','w+')
#f6 = open('test6.txt','w+')
permissionlist = doc.getElementsByTagName('permission')
broadcastlist = doc.getElementsByTagName('protected-broadcast')
actionlist = doc.getElementsByTagName('action')
activitylist = doc.getElementsByTagName('activity')
servicelist = doc.getElementsByTagName('service')
#print>> f, ''.join( [node.data for node in memoryElem.childNodes] )
tmplist1 = []
for p in permissionlist :
   tmplist1.append( p.getAttribute('android:name'))
for b in broadcastlist :
   tmplist1.append( b.getAttribute('android:name'))
for a in actionlist :
    tmplist1.append( a.getAttribute('android:name'))   
for ac in activitylist :
    tmplist1.append( ac.getAttribute('android:name'))
for s in servicelist :
    tmplist1.append( s.getAttribute('android:name'))
for sp in servicelist :
    tmplist1.append( sp.getAttribute('android:permission'))
featurelist = list(set(tmplist1))

for fe in featurelist :
    print >> f1, '@attribute  '+ "'"+fe+"'" +'  '+ "{'0','1'}"
print >> f1, '@attribute   '+"'"+'Class'+"'"+  "   {'benign','malware'}"
print >> f1, '@data'
for r in range(1,99) :
    doc1 = minidom.parse('%s.xml' %r)
    permissionlist = doc1.getElementsByTagName('permission') # and doc1.getElementsByTagName('uses-permission')
    broadcastlist = doc1.getElementsByTagName('protected-broadcast')
    useslist = doc1.getElementsByTagName('uses-permission')
    actionlist = doc1.getElementsByTagName('action')
    activitylist = doc1.getElementsByTagName('activity')
    receiverlist = doc1.getElementsByTagName('receiver')
    servicelist = doc1.getElementsByTagName('service')
                                                             #print>> f, ''.join( [node.data for node in memoryElem.childNodes] )
    tmplist2 = []
    for p in permissionlist :
       tmplist2.append( p.getAttribute('android:name'))
    for u in useslist :
       tmplist2.append( u.getAttribute('android:name'))
    for re in receiverlist :
       tmplist2.append( re.getAttribute('android:name'))
    for b in broadcastlist :
       tmplist2.append( b.getAttribute('android:name'))
    for a in actionlist :
        tmplist2.append( a.getAttribute('android:name'))   
    for ac in activitylist :
        tmplist2.append( ac.getAttribute('android:name'))
    for s in servicelist :
        tmplist2.append( s.getAttribute('android:name'))
    for sp in servicelist :
        tmplist2.append( sp.getAttribute('android:permission'))
    featurelist1 = []
    featurelist1 =list( set(tmplist2))
  
   # o = '%s.txt' %r
    #f2 = open(o,'w+')
    #for kk in featurelist1:
     #   print >> f2,kk    
    #f1.write('\n')
    tmp = []
    for k in featurelist :
       tmp.append('0,')   
    l = 0 
    for i in featurelist :
        for j in featurelist1 :
            if i==j:
                tmp[l] = '1,'
                break
        l = l+1
    for j in tmp:
       f1.write(j)  
    print >> f1 ,'benign'      
 #   print >> f1 , len(tmp)

for r in range(1,104) :
    doc1 = minidom.parse('malwarexml/%s.xml' %r)
    permissionlist = doc1.getElementsByTagName('permission') # and doc1.getElementsByTagName('uses-permission')
    broadcastlist = doc1.getElementsByTagName('protected-broadcast')
    useslist = doc1.getElementsByTagName('uses-permission')
    actionlist = doc1.getElementsByTagName('action')
    activitylist = doc1.getElementsByTagName('activity')
    receiverlist = doc1.getElementsByTagName('receiver')
    servicelist = doc1.getElementsByTagName('service')
                                                             #print>> f, ''.join( [node.data for node in memoryElem.childNodes] )
    tmplist2 = []
    for p in permissionlist :
       tmplist2.append( p.getAttribute('android:name'))
    for u in useslist :
       tmplist2.append( u.getAttribute('android:name'))
    for re in receiverlist :
       tmplist2.append( re.getAttribute('android:name'))
    for b in broadcastlist :
       tmplist2.append( b.getAttribute('android:name'))
    for a in actionlist :
        tmplist2.append( a.getAttribute('android:name'))   
    for ac in activitylist :
        tmplist2.append( ac.getAttribute('android:name'))
    for s in servicelist :
        tmplist2.append( s.getAttribute('android:name'))
    for sp in servicelist :
        tmplist2.append( sp.getAttribute('android:permission'))
    featurelist1 = []
    featurelist1 =list( set(tmplist2))
  

    tmp = []
    for k in featurelist :
       tmp.append('0,')   
    l = 0 
    for i in featurelist :
        for j in featurelist1 :
            if i==j:
                tmp[l] = '1,'
                break
        l = l+1
    for j in tmp:
       f1.write(j)  
    print >> f1 ,'malware'      
 #   print >> f1 , len(tmp)
f1.close()
    #print "____________**************************_____________"   
 
            
        
