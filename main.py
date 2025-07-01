# Programa con while y 3 opciones

while True:
    print("\nElige una opción de la lista:")
    print("1 - Breve historia")
    print("2 - Habitantes")
    print("3 - Sitios turísticos")
    print("4 - Salir")

    opcion = input("\nEscoge una opción: ")

    if opcion == "1":
        historia = ("\nMaturín, capital del estado Monagas en Venezuela, fue fundada el 7 de diciembre de 1760 por el fraile capuchino Lucas de Zaragoza como un pueblo de misión para indígenas Guaraunos, bajo el nombre de San Judas Tadeo de Maturín. Sin embargo, existe evidencia de una fundación anterior en 1722, llamada San Juan de la Tornera de Maturín, aunque esta no prosperó. Maturín se desarrolló a partir de estas misiones y eventualmente se convirtió en un importante centro urbano.")
        print(historia)

    elif opcion == "2":
        habitantes = ("La población de Maturín supera los 655.000 habitantes.")
        print(habitantes)

    elif opcion == "3":
        sitios = ("Tres lugares turísticos importantes en Maturín son la Catedral de Maturín, el Parque Zoológico La Guaricha y el Estadio Monumental de Maturín.")
        print(sitios)

#Salir???
    
    else:
        print("Opción inválida. Saliendo del programa...")
        break


#cambio hecho el primer dia del mes 01/07/25
