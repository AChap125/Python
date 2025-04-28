class Employee:
    def __init__(self, name, number):
        self._name = name
        self._number = number

    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self._shift_number = shift_number
        self._hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self._shift_number

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_shift_number(self, shift_number):
        self._shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate = hourly_pay_rate
