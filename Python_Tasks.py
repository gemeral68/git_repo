
y=input('Введите номер vlan: ')
f=open('config.txt')
for strings in f:
        x=str.split(f.readline())
        if len(x)>3 and len(x[1])>12 and x[0] == y:
                        vlan,mac,state,intf = x
                        print("{:<5} {:>15} {:>10}".format(vlan, mac, intf))
        
                
 


