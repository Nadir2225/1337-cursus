from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return ("Output: " + result)


class NumericProcessor(DataProcessor):
    def validate(self, data: Optional[List]) -> bool:
        try:
            if len(data) == 0:
                return False
            for num in data:
                int(num)
            return True
        except Exception:
            return False

    def process(self, data: Any) -> str:
        return (f'Processed {len(data)} numeric values,' +
                f' sum={sum(data)}, avg={sum(data) / len(data)}')

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if data is None:
                return False
            str(data)
            return True
        except (ValueError, TypeError):
            return False

    def process(self, data: Any) -> str:
        return (
            f'Processed text: {len(data)} characters,'
            f' {len(data.split())} words'
        )


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if data is None:
                return False
            str(data)
            return True
        except (ValueError, TypeError):
            return False

    def process(self, data: Any) -> str:
        return data


if __name__ == '__main__':
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    numP = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    if numP.validate(data):
        print('Validation: Numeric data verified')
    msg = numP.format_output(numP.process(data))
    print(msg)
    print()

    print("Initializing Text Processor...")
    textP = TextProcessor()
    data = "Hello Nexus World"
    print(f"Processing data: \"{data}\"")
    if textP.validate(data):
        print('Validation: Text data verified')
        msg = textP.format_output(textP.process(data))
        print(msg)
    print()

    print("Initializing Log Processor...")
    logP = LogProcessor()
    data = "ERROR: Connection timeout"
    print(f"Processing data: \"{data}\"")
    if logP.validate(data):
        print('Validation: Log entry verified')
        msg = logP.format_output(
            logP.process("[ALERT] ERROR level detected: Connection timeout")
        )
        print(msg)
    print()

    print("=== Polymorphic Processing Demo ===")
    proc_datas: List[Dict[DataProcessor, Union[int, List[int], str]]] = [
        {
            "process": numP,
            "batch": [1, 2, 3]
        },
        {
            "process": textP,
            "batch": "Hello World!"
        },
        {
            "process": logP,
            "batch": "[INFO] INFO level detected: System ready"
        }
    ]
    print("Processing multiple data types through same interface...")
    i = 1
    for proc_data in proc_datas:
        res = proc_data["process"].process(proc_data["batch"])
        print(f"Result {i}: {res}")
        i += 1
    print()

    print("Foundation systems online. Nexus ready for advanced streams.")
