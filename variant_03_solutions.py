"""
Лабораторна робота: Варіант 3
Студент: Межинський Іван
Група: EIP-30
"""

# Задача 1: Класифікатор атмосферних зон (if/elif/else)
def classify_atmosphere(h_km: float) -> tuple:
    """
    Визначає зону за висотою h_km:
    - h <= 11 -> ("Тропосфера", "Метеозонд")
    - 11 < h <= 50 -> ("Стратосфера", "Стратостат / Лідар")
    - 50 < h <= 85 -> ("Мезосфера", "Метеоракета")
    - h > 85 -> ("Термосфера", "Малий супутник")
    """
    if h_km<=11:
        return ("Тропосфера", "Метеозонд")
    elif h_km<=50: 
        return ("Стратосфера", "Стратостат / Лідар")
    elif h_km<=85:
        return ("Мезосфера", "Метеоракета")
    else:
        return ("Термосфера", "Малий супутник")
a=int(input()) 
if a==1:     # Тестування всіх можливих варіантів 
    print("================Тестування завдання 1.1================")
    print(f"Зона атмосфери за висотою: {classify_atmosphere(3.7)[0]}, Прилад вимірювання: {classify_atmosphere(3.7)[1]}")   
    print(f"Зона атмосфери за висотою: {classify_atmosphere(13.2)[0]}, Прилад вимірювання: {classify_atmosphere(13.2)[1]}")  
    print(f"Зона атмосфери за висотою: {classify_atmosphere(59.6)[0]}, Прилад вимірювання: {classify_atmosphere(59.6)[1]}")  
    print(f"Зона атмосфери за висотою: {classify_atmosphere(100)[0]}, Прилад вимірювання: {classify_atmosphere(100)[1]}")  

# Задача 2: Парсер кадрів CAN (match-case)
def parse_can_frame(frame: list) -> str:
    """
    Приймає [can_id, payload_bytes].
    - can_id == 0x10 та len(payload) == 8 -> "Навігація: Повний кадр"
    - can_id == 0x20 та len(payload) == 8 -> "Керування двигуном: Повний кадр"
    - can_id 0x10 або 0x20 з іншою довжиною -> "Помилка довжини кадру"
    - інше -> "Невідомий CAN ID"
    """
    match frame:
        case [0x10, payload] if len(payload)==8:
            return "Навігація: Повний кадр"
        case [0x20, payload] if len(payload)==8:
            return "Керування двигуном: Повний кадр"
        case [0x10|0x20, _]: 
            return "Помилка довжини кадру"
        case other:
            return "Невідомий CAN ID"
if a==2:
    print(parse_can_frame([0x10, [1,0,0,1,0,1,1,0]]))
    print(parse_can_frame([0x20, "10010110"]))
    print(parse_can_frame([0x10, [1,0,0,1,0,1,1]]))
    print(parse_can_frame([0x101, [1,0,0,1,0,1,1]]))

# Задача 3: Моделювання розрядки акумулятора (while / break)
def simulate_battery(start_voltage: float, emergency_flag: bool = False) -> tuple:
    """
    Зменшує напругу на 0.05 В за кожен виток.
    Цикл зупиняється при V < 3.3 В або за прапорцем emergency_flag (після 5 витків).
    Повертає кортеж (кількість_витків, кінцева_напруга).
    """
    orbit=0
    while start_voltage>=3.3 and not (emergency_flag and orbit>=5):          #>=3.3 бо через особливості заокруглення float віднімається число трішки менше за 0.05
        orbit+=1
        start_voltage-=0.05
        start_voltage=round(start_voltage, 3)
    return (orbit, start_voltage)
if a==3:
    print(simulate_battery(4.2, False))
    print(simulate_battery(4.2, True))

# Задача 4: Фільтр ковзного середнього (range / len)
def smooth_gyro_data(data: list) -> list:
    """
    Обчислює згладжений масив середнім арифметичним трьох послідовних вимірів
    через індексацію range(len(data) - 2).
    """
    smooth=[]
    data=list(map(float, data))
    for i in range(len(data) - 2):
        window=(data[i:i+3])
        ave=sum(window)/3
        smooth.append(round(ave,2))
    return (smooth)    
if a==4:
    print(smooth_gyro_data([0.1, 0.15, 0.8, 0.12, 0.11, 0.95, 0.13, 0.14]))