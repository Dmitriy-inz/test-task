class Phone:
    # Вот здесь объявлен атрибут класса.
    line_type = 'проводной'

    # Это инициализатор класса, в котором объявлено два параметра.
    def __init__(self, dial_type_value):
        # Вот он - атрибут объекта.
        self.dial_type = dial_type_value


rotary_phone = Phone()
keypad_phone = Phone()

print(rotary_phone.line_type)
