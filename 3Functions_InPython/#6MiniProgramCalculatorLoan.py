def emiCalculator(principal,rate,time):
    r=rate/12/100
    emi= (principal*r*(1+r)**time)/((1+r)**time-1)
    return emi


monthly_Payment=emiCalculator(1000,10.75,240)

print(f"The monthly payment is : {monthly_Payment}")