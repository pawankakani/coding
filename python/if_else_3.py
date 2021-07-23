temperature = int(input("Enter temperature in degrees celcius : "))

if temperature > 35:        ## <1>
    print("It is very hot")
elif temperature > 15:      ## <2>
    print("It is pleasant")
else:                       ## <3>
    print("It is very cold")


