import math

area = 0

while True:

    print('==================')
    print('Area Calculator 📐')
    print('==================')
    print('')
    print('1) Triangle')
    print('2) Rectangle')
    print('3) Square')
    print('4) Circle')
    print('5) Quit')
    print('')

    inputShape = int(input('Which shape: '))
    print('')

    if inputShape == 1:
        inputBase = int(input('Base: '))
        inputHeight = int(input('Height: '))
        area = (inputHeight * inputBase) / 2
        print(f'The area of the triangle is: {area}')
    elif inputShape == 2:
        inputLength = int(input('Length: '))
        inputWidth = int(input('Width: '))
        area = (inputLength * inputWidth)
        print(f'The area of the rectangle is: {area}')
    elif inputShape == 3:
        inputSide = int(input('Side: '))
        area = (inputSide**2)
        print(f'The area of the square is: {area}')
    elif inputShape == 4:
        inputRadius = int(input('Radius: '))
        area = math.pi * (inputRadius**2)
        print(f'The area of the circle is: {area}')
    elif inputShape == 5:
        print('Bye')
        break
    else:
        print('Invalid input')
        print('')