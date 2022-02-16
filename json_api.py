import json
import controller_handler
import api_client

# Zczytywanie danych działa - poprawić format danych
data = controller_handler.Controller(port='COM3', baud_rate=115200, how_many_data=10).read_data_from_port()
temp_data = [elem[1] for elem in data]
fotor_data = [elem[0] for elem in data]

print(temp_data)

# measurements_type_temp = {"type": "Temperature",
#                      "value": 50,
#                      "unit": "oC",
#                      "timestamp": "2022-02-14T18:59:36+00:00"}
#
# measurements_type_fotor = {"type": "Fotoresistor",
#                      "value": 50,
#                      "unit": "mV",
#                      "timestamp": "2022-02-14T18:59:36+00:00"}

dict_structure = {
    "program_id": "kod",
    "sensor_type": "DHT11",
    "ucontroller": "Arduino UNO",
    "serial_port_number": 3,
    "baud_rate": 115200,
    "measurements": ["measurements_type", "measurements_type"]
}

y = json.dumps(dict_structure)

print(y)
