from collections import namedtuple
import serial
from typing import List, Tuple
from datetime import datetime, date

Data = namedtuple('Data', ['type', 'value', 'unit', 'date'])


class Controller:
    def __init__(self, port: str, baud_rate: int, how_many_data: int):
        self.port: str = port
        self.baud_rate: int = baud_rate
        self.how_many_data: int = how_many_data
        self.buffer: List[Tuple[Data]] = list()

    def read_data_from_port(self):
        serial_port = serial.Serial(port=self.port, baudrate=self.baud_rate)
        while len(self.buffer) < self.how_many_data:
            line = serial_port.readline().decode('ascii')
            data = self.extract_data(line)
            self.buffer.append(data)
        return self.buffer

    @classmethod
    def extract_data(cls, line: str):
        line = line.split(sep=',')
        split_fotorezystor = line[0].split(sep=': ')
        split_temp = line[1].split(sep=': ')
        date = datetime.now().isoformat()

        fotorezystor = Data(split_fotorezystor[0], split_fotorezystor[1], 'mV', timestamp)
        temperatura = Data(split_temp[0], split_temp[1], 'oC', date)
        return fotorezystor, temperatura

    def get_baud_rate(self):
        return self.baud_rate

    def get_port(self):
        return self.port
