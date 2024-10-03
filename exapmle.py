def CEL_CONVERTER_FER(Celsius):
    Farenheit=(Celsius * 9/5) + 32 
    return "the teampreture "+str(Celsius)+"Farenheit degree is "+ str(Farenheit)


celsius=float(input("enter what the teampreture in celsuis"))
print(CEL_CONVERTER_FER(celsius))
if celsius>38:
    print("you have fever")  # This line will always run, regardless of the value of
else:
    print("you are normal")  # This line will only run if the value of celsius