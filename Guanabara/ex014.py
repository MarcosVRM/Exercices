# conver sor de celcius para fahrenheit e kelvin
print('Conversor de temperatura\n', '-' * 30)
ce = float(input('Digite a temperatura a ser convertida, em graus celcius: '))
fah = ce * (9 / 5) + 32
kel = ce + 273.15
print('~' * 30)
print('{:.1f}°C convertido para fahrenheit {:.1f}°F e em kelvin {:.1f}°K'.format(ce, fah, kel))
