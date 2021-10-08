def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32) * 5/9

celsius = float(input("Indica los grados que deseas convertir a fahrenheit: "))
fahrenheit = float(input("Indica los grados que deseas convertir a celsius: "))

print(f"Celcius en Farhrenheit: {celsius_fahrenheit(celsius)}")
print(f"Fahrenheit en Celcius: {fahrenheit_celsius(fahrenheit)}")