import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app.arhive_model import Base, Arhive  # Replace 'your_module' with your module name


class TestArhiveModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up an in-memory SQLite database for testing
        cls.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(cls.engine)  # Create all tables
        cls.Session = sessionmaker(bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        # Dispose of the engine after tests
        cls.engine.dispose()

    def setUp(self):
        # Start a new session for each test
        self.session = self.Session()

    def tearDown(self):
        # Rollback the session and close it after each test
        self.session.rollback()
        self.session.close()

    def test_arhive_table_columns(self):
        """Test that the Arhive table columns are defined correctly."""
        self.assertEqual(Arhive.__tablename__, "arhive")
        self.assertTrue(hasattr(Arhive, "rowid"))
        self.assertTrue(hasattr(Arhive, "idDevice"))
        self.assertTrue(hasattr(Arhive, "idChannel"))
        self.assertTrue(hasattr(Arhive, "value"))
        self.assertTrue(hasattr(Arhive, "time"))
        self.assertTrue(hasattr(Arhive, "strTime"))

    def test_create_arhive_instance(self):
        """Test creating an instance of the Arhive model."""
        record = Arhive(
            idDevice="Device123",
            idChannel="Channel456",
            value="SampleValue",
            time=1672500000,
            strTime=datetime(2025, 1, 28, 12, 34, 56),
        )
        self.assertEqual(record.idDevice, "Device123")
        self.assertEqual(record.idChannel, "Channel456")
        self.assertEqual(record.value, "SampleValue")
        self.assertEqual(record.time, 1672500000)
        self.assertEqual(record.strTime, datetime(2025, 1, 28, 12, 34, 56))

    def test_insert_arhive_record(self):
        """Test inserting a record into the Arhive table."""
        record = Arhive(
            idDevice="Device123",
            idChannel="Channel456",
            value="SampleValue",
            time=1672500000,
            strTime=datetime(2025, 1, 28, 12, 34, 56),
        )
        self.session.add(record)
        self.session.commit()

        # Fetch the record from the database
        fetched_record = self.session.query(Arhive).first()
        self.assertIsNotNone(fetched_record)
        self.assertEqual(fetched_record.idDevice, "Device123")
        self.assertEqual(fetched_record.idChannel, "Channel456")

    def test_primary_key_constraint(self):
        """Test that the rowid column is a primary key."""
        record1 = Arhive(
            idDevice="Device123",
            idChannel="Channel456",
            value="Value1",
            time=1672500000,
            strTime=datetime(2025, 1, 28, 12, 34, 56),
        )
        self.session.add(record1)
        self.session.commit()

        with self.assertRaises(IntegrityError):
            # Try inserting another record with the same rowid (manually set)
            record2 = Arhive(
                rowid=1,  # Duplicate primary key
                idDevice="Device789",
                idChannel="Channel890",
                value="Value2",
                time=1672500001,
                strTime=datetime(2025, 1, 28, 12, 35, 0),
            )
            self.session.add(record2)
            self.session.commit()

    def test_repr_method(self):
        """Test the __repr__ method for debugging output."""
        record = Arhive(
            rowid=1,
            idDevice="Device123",
            idChannel="Channel456",
            value="SampleValue",
            time=1672500000,
            strTime=datetime(2025, 1, 28, 12, 34, 56),
        )
        expected_repr = (
            "<Arhive(rowid=1, idDevice=Device123, idChannel=Channel456, "
            "value=SampleValue, time=1672500000, strTime=2025-01-28 12:34:56)>"
        )
        self.assertEqual(repr(record), expected_repr)


if __name__ == "__main__":
    unittest.main()
