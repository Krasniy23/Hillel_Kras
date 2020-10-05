def get_velue():
    temperature_value = int(input('Enter value:'))
    temperature_type = int(input('Enter type:'))
    return temperature_calc(temperature_value, temperature_type)


def temperature_calc(temperature_value, temperature_type):
    if temperature_type not in ('K', 'C', 'F'):
        print('Wrong type!')
    if temperature_type == 'K':
        k = temperature_value
        c = temperature_value + 273.15
        f = int((temperature_value + 459.67) / 1.8)
    elif temperature_type == 'C':
        c = temperature_value
        k = temperature_value - 273.15
        f = int((temperature_value - 32) / 1.8)
    elif temperature_type == 'F':
        f = temperature_value
        k = int((temperature_value + 459.67) / 1.8)
        c = int((temperature_value - 32) / 1.8)
        print(f'Kelvin {k} degrees', f'Celsius {c} degrees', f'Fahrenheits {f} degrees')


get_velue()