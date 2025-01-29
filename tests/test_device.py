import unittest
from collections import namedtuple

from app.services.device import Device


class TestDevice(unittest.TestCase):
    def setUp(self):
        # Create a mock Arhive record structure
        self.Record = namedtuple("Record", ["idChannel", "value", "time"])

        # Example records to test
        self.records = [
            self.Record(idChannel=1, value="A", time=100),
            self.Record(idChannel=2, value="B", time=200),
            self.Record(idChannel=1, value="C", time=150),
            self.Record(idChannel=2, value="D", time=250),
            self.Record(idChannel=3, value="E", time=300),
        ]

    def test_get_devices_with_valid_data(self):
        # Act
        devices = Device.get_devices(self.records)

        # Assert
        self.assertEqual(len(devices), 3)  # Expecting 3 unique idChannels

        # Validate each device
        self.assertEqual(devices[0].id, 1)
        self.assertEqual(devices[0].values, ["A", "C"])
        self.assertEqual(devices[0].time, [100, 150])

        self.assertEqual(devices[1].id, 2)
        self.assertEqual(devices[1].values, ["B", "D"])
        self.assertEqual(devices[1].time, [200, 250])

        self.assertEqual(devices[2].id, 3)
        self.assertEqual(devices[2].values, ["E"])
        self.assertEqual(devices[2].time, [300])

    def test_get_devices_with_empty_data(self):
        # Act
        devices = Device.get_devices([])

        # Assert
        self.assertEqual(len(devices), 0)  # No records should result in no devices

    def test_get_devices_with_single_record(self):
        # Arrange
        single_record = [self.Record(idChannel=1, value="A", time=100)]

        # Act
        devices = Device.get_devices(single_record)

        # Assert
        self.assertEqual(len(devices), 1)
        self.assertEqual(devices[0].id, 1)
        self.assertEqual(devices[0].values, ["A"])
        self.assertEqual(devices[0].time, [100])

if __name__ == "__main__":
    unittest.main()
