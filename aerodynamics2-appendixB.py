import math

def normal_shock_properties(M1):
    gamma = 1.4
    M2 = math.sqrt(((gamma-1)*M1**2+2)/(2*gamma*M1**2-(gamma-1)))
    p2_p1 = ((2*gamma*(M1**2))-(gamma-1))/(gamma+1)
    roh2_roh1 =(gamma+1)*(M1**2)/((gamma-1)*(M1**2)+2)
    t2_t1 = (1+(2*gamma/(gamma+1))*(M1**2-1))*((2+(gamma-1)*(M1**2))/((gamma+1)*M1**2))
    p02_p1 = ((gamma+1)**2*M1**2/(4*gamma*M1**2-2*(gamma-1)))**(gamma/(gamma-1))*(1-gamma+2*gamma*M1**2)/(gamma+1)

    return round(M1,3),round(p2_p1,3),round(roh2_roh1,3),round(t2_t1,3),round(p02_p1,3),round(M2,3)

print("{:^60}".format("NORMAL SHOCK PROPERTIES"))
print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format("M1","P2/P1","roh2/roh1","T2/T1","P02/P1","M2"))
print("-"*70)

for M1 in [x/1000 for x in range(1000,50001,20)]:
    M1,p2_p1,roh2_roh1,t2_t1,p02_p1,M2 = normal_shock_properties(M1)
    print("{:<15.3f}{:<15.3f}{:<15.3f}{:<15.3f}{:<15.3f}{:<15.3f}".format(M1,p2_p1,roh2_roh1,t2_t1,p02_p1,M2))