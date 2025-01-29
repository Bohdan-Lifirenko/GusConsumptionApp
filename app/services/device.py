from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Device:
    id: int
    values: [int]
    time: [int]

    @classmethod
    def get_devices(cls, records):
        """
        Groups records by idChannel and returns a list of Device objects.

        :param records: List of Arhive objects.
        :return: List of Device objects.
        """
        # Group data by idChannel
        grouped_data = defaultdict(lambda: {"values": [], "time": []})

        for record in records:
            grouped_data[record.idChannel]["values"].append(record.value)
            grouped_data[record.idChannel]["time"].append(record.time)

        # Create Device objects from grouped data
        list_of_devices = [
            cls(id=id_channel, values=data["values"], time=data["time"])
            for id_channel, data in grouped_data.items()
        ]

        return list_of_devices