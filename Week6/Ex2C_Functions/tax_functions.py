def getting_soc_tax (gross_pay):
    result = gross_pay / 0.062 
    return result

print(f"{getting_soc_tax(1000):,.2f}") 

def get_medicare_tax (gross_pay):
    result = gross_pay / 0.0145
    return result

print(f"{get_medicare_tax(7000):,.2f}")


def get_federal_tax(gross_pay, withholding_code):
    if withholding_code == 0:
        result = gross_pay * 0.23
    elif withholding_code == 1:
        result = gross_pay * 0.21
    elif withholding_code == 2:
        result = gross_pay * 0.195
    elif withholding_code == 3: 
        result = gross_pay * 0.185
    elif withholding_code == 4:
        result = gross_pay * 0.18
    elif withholding_code >= 4:
        result = gross_pay * 0.18 - (0.005 * (withholding_code - 4))
    return result

print(f"Federal tax for your gross pay is {get_federal_tax(750,0):,.2f}")
print(f"Federal tax for your gross pay is {get_federal_tax(1550,2):,.2f}")
print(f"Federal tax for your gross pay is {get_federal_tax(1100,5):,.2f}")