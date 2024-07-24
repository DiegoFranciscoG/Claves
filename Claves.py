import random

def generar_contraseña(longitud):
  caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
  contraseña = ""
  for _ in range(longitud):
    contraseña += random.choice(caracteres)
  return contraseña

longitud = int(input("Introduce la longitud de la contraseña: "))
contraseña = generar_contraseña(longitud)
print("Tu contraseña generada es:", contraseña)