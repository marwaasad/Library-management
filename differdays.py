import datetime
from datetime import date
def differdays(p,q):
    d0=date(int(p[0:4]),int(p[5:7]),int(p[8:10]))
    d1=date(int(q[0:4]),int(q[5:7]),int(q[8:10]))
    print('today',int(p[0:4]),'-',int(p[5:7]),'-',int(p[8:10]))
    print('return date',int(q[0:4]),'-',int(q[5:7]),'-',int(q[8:10]))
    delta=d0-d1      
    print('number of days done away=',delta.days)
    return delta.days