from reportlab.pdfgen import canvas


def To_Dictionary(data: str) -> dict:
    array = data.split(',')
    key = array[0]
    value = \
        {
            "Nombre": array[1],
            "Fecha": array[2],
            "Movimientos": array[3],
            "Copas": int(array[4])
        }

    return {key: value}


def Read_File() -> dict:
    file = open("Data/BaseData.txt", 'r')
    info = {}

    for data in file:
        data = data.strip()
        info.update(To_Dictionary(data))

    file.close()

    return info


def Write_File(data: dict):
    players_info = dict()
    players_info.update(Read_File())
    players_info.update(data)

    file = open("Data/BaseData.txt", 'w')

    info = ""
    for key, value in players_info.items():
        info += f"{key},"

        for key_1, value_1 in value.items():
            if key_1 != "Copas":
                info += str(value_1) + ","
            else:
                info += str(value_1)

        info += "\n"

    file.write(info)
    file.close()


def Search_Per_Month(month: str) -> list:
    def Get_Month(message: str) -> int:
        info = message.split(',')
        month = info[2].split('-')
        return int(month[0])

    def Convert_To_Month(month: str) -> str:
        month = month.lower()
        months = {
            'enero': 1,
            'febrero': 2,
            'marzo': 3,
            'abril': 4,
            'mayo': 5,
            'junio': 6,
            'julio': 7,
            'agosto': 8,
            'septiembre': 9,
            'octubre': 10,
            'noviembre': 11,
            'diciembre': 12
        }

        return months[month]

    def Linear_Search(array: list, value: str) -> bool:
        value = Convert_To_Month(value)

        for i in range(len(array)):
            month = Get_Month(array[i])
            if month == value:
                return True, i
        return False, -1

    file = open("Data/BaseData.txt", 'r')
    array = []
    info = []

    for data in file:
        data = data.strip()
        array.append(data)

    while Linear_Search(array, month)[0]:
        index = Linear_Search(array, month)[1]
        temp = array[index].split(',')
        info.append(temp)
        del array[index]

    return info


def Get_Player(ID: str) -> dict:
    aux_dict = Read_File()

    if ID in aux_dict:
        return aux_dict[ID]
    return -1


def Sort_File() -> list:
    def Get_Movements(message: str) -> int:
        info = message.split(',')
        array = info[-2].split('-')
        return array[-1]

    def Bubble_Sort(array: list):
        for tope in range(len(array) - 1, 0, -1):
            for i in range(tope):
                value_1 = Get_Movements(array[i])
                value_2 = Get_Movements(array[i + 1])
                if value_1 > value_2:
                    temp = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = temp

    file = open("Data/BaseData.txt", 'r')
    array = []
    info = []

    for data in file:
        data = data.strip()
        array.append(data)

    Bubble_Sort(array)

    for i in range(len(array)):
        temp = array[i].split(',')
        del temp[-2]
        info.append(temp)

    return info


def Export_PDF(ID: str):
    m_canvas = canvas.Canvas("BaseData.pdf")

    coord_x = 100
    coord_y = 750
    line_space = 20

    file = open("Data/BaseData.txt", 'r')

    data = Get_Player(ID)

    m_canvas.drawString(coord_x, coord_y, f"E-mail: {ID}")
    m_canvas.drawString(coord_x, coord_y - line_space, f"Nombre: {data['Nombre']}")
    m_canvas.drawString(coord_x, coord_y - 2 * line_space, f"Fecha: {data['Fecha']}")
    m_canvas.drawString(coord_x, coord_y - 3 * line_space, f"Movimientos: {data['Movimientos']}")
    m_canvas.drawString(coord_x, coord_y - 4 * line_space, f"Cantidad de veces que gano: {data['Copas']}")

    m_canvas.save()