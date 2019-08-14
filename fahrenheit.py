while True:
    try:
        celsiusInput = float(input ("Input Celsius: "))
        fahrenheitOutput = 1.8*celsiusInput+32
        print("Fahrenheit:" , fahrenheitOutput)
        import sys
        sys.exit()
    except ValueError:
        print("Fooey! That's not a number!")
