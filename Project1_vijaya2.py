a=input("Enter the numbers:")
a=a.split(",")
for i in a:
    d=[]
    if(i[-1] in "02468"):
        d.append(2)
    s3=0
    ss3=str(i)
    if(i=="3"):
        d.append(3)
    if(len(i)>1):
        while(len(str(ss3))!=1):
            for k in range(len(str(ss3))):
                z=str(ss3)
                s3=s3+int(z[k])
            ss3=s3
            s3=0
        s3=str(ss3)
        if s3[-1] in "369":
            d.append(3)
    if(len(i)==1 and i in "48"):
        d.append(4)
    if((len(i)>1) and ((i[-2] in "02468" and i[-1] in "048") or (i[-2] in "13579" and i[-1] in "26"))):
        d.append(4)
    if(i[-1] in "05"):
        d.append(5)
    if( 2 in d and 3 in d):
        d.append(6)
    if(i==7):
        d.append(7)
    if(len(i)>1):
        tt=i
        while(len(str(tt))!=1):
            t1=str(tt)
            t1=t1[:-1]
            t2=str(tt)
            t2=t2[-1]
            t2=int(t2)*2
            tt=abs(int(t1)-t2)
        if(tt==7 or tt==0):
            d.append(7)
    if(i==8):
        d.append(8)
    if(len(i)>1):
        t=i
        while(len(str(t))!=1):
            t1=i[:-1]
            t2=i[-1]
            t=(int(t1)*2)+int(t2)
        if(t==8 or t==0):
            d.append(8)
        print(d)
    if(i==9):
        d.append(9)
    if(len(i)>1):
        s3=0
        ss3=str(i)
        while(len(str(ss3))!=1):
            for k in range(len(str(ss3))):
                z=str(ss3)
                s3=s3+int(z[k])
            ss3=s3
            s3=0
        if(s3==9 or s3==0):
            d.append(9)
    if(d):
        print(i," divisible  by",d)
    else:
        print(i," is not divisible ")
 
