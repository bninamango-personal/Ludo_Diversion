# from reportlab.pdfgen import canvas
#
#
# def exportar_a_pdf(nombre_archivo, datos):
#     c = canvas.Canvas(nombre_archivo + ".pdf")
#
#     # Convertir los datos en una lista de líneas
#     lineas = datos.split("\n")
#
#     # Configurar las coordenadas y el espacio entre líneas
#     x = 100
#     y = 750
#     espacio_linea = 20
#
#     # Agregar cada línea al PDF
#     for linea in lineas:
#         c.drawString(x, y, linea)
#         y -= espacio_linea
#
#     c.save()
#
#
# # Datos a exportar
# datos = """bryan140101@gmail.com, Bryan , 10-2023, 6-6-6-2 , 1
# bninamango.personal@gmail.com, Bryannsss , 10-2025,7-8-9-6, 2"""
#
# # Formatear los datos para que se muestren correctamente en el PDF
#
# datos_formateados = ""
# for linea in datos.split("\n"):
#     datos_linea = linea.split(",")
#     email = datos_linea[0]
#     nombre = datos_linea[1]
#     fecha = datos_linea[2]
#     pasos = datos_linea[3]
#     pasos_str = ", ".join(pasos.strip("-").split())
#     ganador = datos_linea[4]
#
#     datos_formateados += f"Email: {email}\n"
#     datos_formateados += f"Nombre: {nombre}\n"
#     datos_formateados += f"Fecha: {fecha}\n"
#     datos_formateados += f"Pasos del ganador: {pasos_str}\n"
#     datos_formateados += f"Cantidad de veces que gano : {ganador}\n\n"
#
# # Llamada a la función para exportar a PDF
# exportar_a_pdf("mi_archivo", datos_formateados)



from reportlab.pdfgen import canvas

def exportar_a_pdf(nombre_archivo, datos):
    c = canvas.Canvas(nombre_archivo + ".pdf")

    # Configurar las coordenadas y el espacio entre líneas
    x = 100
    y = 750
    espacio_linea = 20

    # Agregar cada línea de datos al PDF
    for linea in datos.split("\n"):
        campos = linea.split(",")
        c.drawString(x, y, f"Email: {campos[0]}")
        c.drawString(x, y - espacio_linea, f"Nombre: {campos[1]}")
        c.drawString(x, y - 2 * espacio_linea, f"Fecha: {campos[2]}")
        c.drawString(x, y - 3 * espacio_linea, f"Pasos del ganador: {campos[3]}")
        c.drawString(x, y - 4 * espacio_linea, f"Cantidad de veces que ganó: {campos[4]}")
        y -= 6 * espacio_linea

    c.save()


# Datos a exportar
datos = """bryan140101@gmail.com,Bryan,10-2023,6-6-6-2,1
bninamango.personal@gmail.com,Bryannsss,10-2025,7-8-9-6,2"""

# Llamada a la función para exportar a PDF
exportar_a_pdf("mi_archivo", datos)
