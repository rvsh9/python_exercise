# hexadecimal to decimal 

def hex_to_decimal_conversion():
    decimal_value = 0

    hex_input = input("Enter hexadecimal :")

    for index,value in enumerate(reversed(hex_input)):
        decimal_value +=  int(value,base=16) * (16 ** index)

    print(f'decimal value for {hex_input} = {decimal_value}')

    return decimal_value

hex_to_decimal_conversion()