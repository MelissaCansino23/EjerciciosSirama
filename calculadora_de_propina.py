print("Bienvenidos a la pantalla de propina")

total_factura = float(input("cuanto te salio?"))
porcentaje_de_propina = float(input("Escoje el %: 10, 12 o 15: "))
numero_de_personas = int(input("cuantas personas comieron?"))

propina = float(total_factura) * (float(porcentaje_de_propina)/100)
total_propina = propina/int(numero_de_personas)
total_propina_redondeada = round(total_propina, 2)

total_a_pagar_por_persona = round((total_factura + propina)/numero_de_personas, 2)
print(f"Total a pagar de propina por persona: $ {total_propina_redondeada}")
print(f"Total a pagar por persona: $ {total_a_pagar_por_persona}")
