import json
from controller_handler import Controller, Data
from MeasurementsBuilder import ConcreteMeasurementBuilder, Measurement

# Zczytywanie danych działa - poprawić format danych


# temp_data = [elem[1] for elem in data]
con = Controller(port='COM3', baud_rate=115200, how_many_data=10)
data = con.read_data_from_port()


def build_API():
    con = Controller(port='COM3', baud_rate=115200, how_many_data=10)
    data = con.read_data_from_port()
    fotor_data = [elem[0] for elem in data]
    builder = ConcreteMeasurementBuilder()
    builder.microcontroller_name("Arduino Uno")
    builder.sensor_type("DS18B20")
    builder.serial_port_number(con.get_port())
    builder.program_id("fs4fasfasfhj4kdv")
    builder.baud_rate(con.get_baud_rate())
    for temp, fotor in data:
        builder.one_measurement(measurement_type=temp.type,
                                value=temp.value,
                                unit=temp.unit,
                                date=temp.date)

        builder.one_measurement(measurement_type=fotor.type,
                                value=fotor.value,
                                unit=fotor.unit,
                                date=fotor.date)

    return builder.build()


y = build_API()

print(y)

#     return fotoresistor_builder.build()
# dict_structure = {
#     "program_id": "kod",
#     "sensor_type": "DHT11",
#     "ucontroller": "Arduino UNO",
#     "serial_port_number": 3,
#     "baud_rate": 115200,
#     "measurements": [temp_data, fotor_data]
# }

# y = json.dumps(dict_structure)

# print(y)
