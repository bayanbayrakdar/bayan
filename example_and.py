def weather(stat_wether,stat):
    if stat_wether=="raining" and stat=="cold":
        print("take an umbrella and a warm jacket.")
    elif stat_wether=="raining" and stat=="warm":
        print("take an umbrella and a t-shirt.")
    elif stat_wether=="sunny" and stat=="cold":
        print("take a warm jacket and sunglasses.")
    elif stat_wether=="sunny" and stat=="warm":
        print("take a t-shirt and sunglasses.") 
    else:
        print("If it is anything else, stay home!")

stat_wether=input("the wether sunny or raining")
stat=input("the weather cold or warm")
print(weather(stat_wether,stat))

