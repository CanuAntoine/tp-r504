import fonctions as f

print("Hello, World!")

def carre():
  while True:
    a = int(input("Put a number: "))
    print(a**2)

a = float(input("Nombre: "))
b = float(input("Puissance: "))

res = f.puissance(a, b)
print(f"Result: {res}")
