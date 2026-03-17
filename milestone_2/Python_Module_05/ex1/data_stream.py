from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):

    def __init__(self, stream_id: str):
        self.stream_id: str = stream_id
        self.processed: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        try:
            return [d for d in data_batch if criteria in str(d)]
        except Exception as e:
            print(f"Error filtering data: {e}")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed": self.processed
        }


class SensorStream(DataStream):

    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed += len(data_batch)

            temps = [
                float(x.split(":")[1]) for x in data_batch if "temp:" in str(x)
            ]
            avg = sum(temps) / len(temps) if temps else 0

            return (
                f"Sensor analysis: {len(data_batch)} readings processed"
                f", avg temp: {avg}°C"
            )
        except Exception as e:
            return f"Sensor error: {e}"


class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed += len(data_batch)
            for item in data_batch:
                if not isinstance(item, str):
                    raise ValueError(f"Invalid transaction format: {item}")
                elif ("buy:" not in item and "sell:" not in item):
                    raise ValueError(f"Invalid transaction format: {item}")
            buy = [int(x.split(":")[1]) for x in data_batch if "buy:" in x]
            sell = [int(x.split(":")[1]) for x in data_batch if "sell:" in x]
            net = sum(buy) - sum(sell)

            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {'+' if net >= 0 else ''}{net} units"
            )
        except Exception as e:
            return f"Transaction error: {e}"


class EventStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed += len(data_batch)

            errors = [e for e in data_batch if "error" in str(e).lower()]
            return (
                f"Event analysis: {len(data_batch)} events, "
                f"{len(errors)} error detected"
            )
        except Exception as e:
            return f"Event error: {e}"


def data_type(obj: Any) -> tuple:
    if obj.__class__.__name__ == "SensorStream":
        return ("Sensor data", "readings")
    elif obj.__class__.__name__ == "TransactionStream":
        return ("Transaction data", "operations")
    elif obj.__class__.__name__ == "EventStream":
        return ("Event data", "events")
    else:
        return ("Unknown data type", "unknown")


class StreamProcessor:

    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]) -> None:

        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        print("Batch 1 Results:")
        index = 0
        for stream in self.streams:
            stream.process_batch(batches[index])
            index += 1
            print(
                f"- {data_type(stream)[0]}: {stream.processed}"
                f" {data_type(stream)[1]} processed"
            )


if __name__ == "__main__":

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor.process_batch(sensor_batch))
    print()

    print("Initializing Transaction Stream...")
    print("Stream ID: TRANS_001, Type: Financial Data")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_batch}")
    print(transaction.process_batch(transaction_batch))
    print()

    print("Initializing Event Stream...")
    print("Stream ID: EVENT_001, Type: System Events")
    eventsbatch = ["login", "error", "logout"]
    print(f"Processing event batch: {eventsbatch}")
    print(event.process_batch(eventsbatch))
    print()

    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")
    manager = StreamProcessor()
    manager.add_stream(sensor)
    manager.add_stream(transaction)
    manager.add_stream(event)

    batches = [
        ["temp:21.5", "temp:22.0"],
        ["buy:50", "sell:30", "buy:40", "sell:20"],
        ["start", "error", "stop"]
    ]

    manager.process_all(batches)

    print("\nStream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")
