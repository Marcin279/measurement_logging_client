from abc import ABC, abstractmethod
from typing import Tuple, Dict


class Measurement:

    def __init__(self):
        self.measurement: Dict = {
            "programId": "",
            "sensorType": "",
            "microController": "",
            "serialPortNumber": 0,
            "baudRate": 0,
            "measurements": []
        }

    def set_microcontroller_name(self, name: str):
        self.measurement["programID"] = name

    def set_sensor_type(self, type_name: str):
        self.measurement["sensorType"] = type_name

    def set_program_id(self, program_id: str):
        self.measurement["microController"] = program_id

    def set_serial_port_number(self, port_number: int):
        self.measurement["serialPortNumber"] = port_number

    def set_baud_rate(self, baud_rate: int):
        self.measurement["baudRate"] = baud_rate

    def append_measurement_value(self, measurement_type: str, value: int, unit: str, timestamp: str):
        self.measurement["measurements"].append(
            dict(type=measurement_type, value=value, unit=unit, timestamp=timestamp)
        )


class MeasurementBuilder(ABC):

    @abstractmethod
    def microcontroller_name(self, name: str):
        pass

    @abstractmethod
    def sensor_type(self, type_name: str):
        pass

    @abstractmethod
    def program_id(self, program_id: str):
        pass

    @abstractmethod
    def serial_port_number(self, port_number: int):
        pass

    @abstractmethod
    def baud_rate(self, baud_rate: int):
        pass

    @abstractmethod
    def one_measurement(self, measurement_type: str, value: int, unit: str, timestamp: str):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build(self):
        pass


class TemperatureMeasurementBuilder(MeasurementBuilder):

    def __init__(self):
        self.measurement = Measurement()

    def microcontroller_name(self, name: str):
        self.measurement.set_microcontroller_name(name=name)

    def sensor_type(self, type_name: str):
        self.measurement.set_sensor_type(type_name=type_name)

    def program_id(self, program_id: str):
        self.measurement.set_program_id(program_id=program_id)

    def serial_port_number(self, port_number: int):
        self.measurement.set_serial_port_number(port_number=port_number)

    def baud_rate(self, baud_rate: int):
        self.measurement.set_baud_rate(baud_rate=baud_rate)

    def one_measurement(self, measurement_type: str, value: int, unit: str, timestamp: str):
        self.measurement.append_measurement_value(measurement_type=measurement_type,
                                                  value=value,
                                                  unit=unit,
                                                  timestamp=timestamp)

    def reset(self):
        self.measurement = Measurement()

    def build(self):
        return self.measurement
