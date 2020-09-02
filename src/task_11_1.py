"""
Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""

class VideoCard:
    def __init__(self,
                 interface,
                 gpu_manufacturer,
                 gpu,
                 video_memory,
                 video_memory_type,
                 gpu_frequency):
        self.__interface = interface
        self.gpu_manufacturer = gpu_manufacturer
        self.gpu = gpu
        self.video_memory = video_memory
        self.__video_memory_type = video_memory_type
        self.__gpu_frequency = gpu_frequency

    @property
    def interface(self):
        return self.__interface

    @interface.setter
    def interface(self, interface):
        self.__interface = interface

    @property
    def video_memory_type(self):
        return self.__video_memory_type

    @video_memory_type.setter
    def video_memory_type(self, video_memory_type):
        self.__video_memory_type = video_memory_type

    @property
    def gpu_frequency(self):
        return self.__gpu_frequency

    @gpu_frequency.setter
    def gpu_frequency(self, gpu_frequency):
        self.__gpu_frequency = gpu_frequency

    def get_image(self):
        print("view image")

    def get_temp(self):
        print("Temperature")


class MotherBoard:
    def __init__(self,
                 brand,
                 model,
                 processor_support,
                 socket,
                 chipset,
                 form_factor,
                 memory_type):
        self.brand = brand
        self.model = model
        self.__processor_support = processor_support
        self.__socket = socket
        self.__chipset = chipset
        self.form_factor = form_factor
        self.memory_type = memory_type

    @property
    def processor_support(self):
        return self.__processor_support

    @processor_support.setter
    def processor_support(self, processor_support):
        self.__processor_support = processor_support

    @property
    def socket(self):
        return self.__socket

    @socket.setter
    def socket(self, socket):
        self.__socket = socket

    @property
    def chipset(self):
        return self.__chipset

    @chipset.setter
    def chipset(self, chipset):
        self.__chipset = chipset

    def get_temp(self):
        print("Temp motherboard")


class Processor:
    def __init__(self,
                 the_lineup,
                 crystal_code_name,
                 socket,
                 number_of_cores,
                 max_number_of_threads,
                 memory_support):
        self.the_lineup = the_lineup
        self.__crystal_code_name = crystal_code_name
        self.socket = socket
        self.__number_of_cores = number_of_cores
        self.__max_number_of_threads = max_number_of_threads
        self.memory_support = memory_support

    @property
    def crystal_code_name(self):
        return self.__crystal_code_name

    @crystal_code_name.setter
    def crystal_code_name(self, crystal_code_name):
        self.__crystal_code_name = crystal_code_name

    @property
    def number_of_cores(self):
        return self.__number_of_cores

    @number_of_cores.setter
    def number_of_cores(self, number_of_cores):
        self.__number_of_cores = number_of_cores

    @property
    def max_number_of_threads(self):
        return self.__max_number_of_threads

    @max_number_of_threads.setter
    def max_number_of_threads(self, max_number_of_threads):
        self.__max_number_of_threads = max_number_of_threads

    def get_temp(self):
        print("Temperature processor")


class RAM:
    def __init__(self,
                 memory,
                 memory_type,
                 frequency,
                 cas_latency,
                 supply_voltage):
        self.memory = memory
        self.memory_type = memory_type
        self.__frequency = frequency
        self.__cas_latency = cas_latency
        self.__supply_voltage = supply_voltage

    @property
    def frequency(self):
        return self.__frequency

    @frequency.setter
    def frequency(self, frequency):
        self.__frequency = frequency

    @property
    def cas_latency(self):
        return self.__cas_latency

    @cas_latency.setter
    def cas_latency(self, cas_latency):
        self.__cas_latency = cas_latency

    @property
    def supply_voltage(self):
        return self.__supply_voltage

    @supply_voltage.setter
    def supply_voltage(self, supply_voltage):
        self.__supply_voltage = supply_voltage

    def get_temp(self):
        print("Temperature ram")


class PowerSupply:
    def __init__(self,
                 power,
                 power_supply_fan_size,
                 number_of_fans,
                 motherboard_power):
        self.power = power
        self.__power_supply_fan_size = power_supply_fan_size
        self.__number_of_fans = number_of_fans
        self.__motherboard_power = motherboard_power

    @property
    def power_supply_fan_size(self):
        return self.__power_supply_fan_size

    @power_supply_fan_size.setter
    def power_supply_fan_size(self, power_supply_fan_size):
        self.__power_supply_fan_size = power_supply_fan_size

    @property
    def number_of_fans(self):
        return self.__number_of_fans

    @number_of_fans.setter
    def number_of_fans(self, number_of_fans):
        self.__number_of_fans = number_of_fans

    @property
    def motherboard_power(self):
        return self.__motherboard_power

    @motherboard_power.setter
    def motherboard_power(self, motherboard_power):
        self.__motherboard_power = motherboard_power

    def get_temp(self):
        print("Temperature PowerSupply")


class Case:
    def __init__(self,
                 power_supply,
                 type_of_shell,
                 compatible_motherboards,
                 body_color,
                 body_material):
        self.__power_supply = power_supply
        self.__type_of_shell = type_of_shell
        self.compatible_motherboards = compatible_motherboards
        self.body_color = body_color
        self.__body_material = body_material

    @property
    def power_supply(self):
        return self.__power_supply

    @power_supply.setter
    def power_supply(self, power_supply):
        self.__power_supply = power_supply

    @property
    def type_of_shell(self):
        return self.__type_of_shell

    @type_of_shell.setter
    def type_of_shell(self, type_of_shell):
        self.__type_of_shell = type_of_shell

    @property
    def body_material(self):
        return self.__body_material

    @body_material.setter
    def body_material(self, body_material):
        self.__body_material = body_material
