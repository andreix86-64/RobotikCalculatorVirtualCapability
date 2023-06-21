import sys
from abc import ABC

from AbstractVirtualCapability import AbstractVirtualCapability, VirtualCapabilityServer


class CalculatorVirtualCapability(AbstractVirtualCapability, ABC):
    """ Simple calculator to test virtual capabilities """

    def __init__(self, server):
        super().__init__(server)
        self.current_operation = None
        self.a = None
        self.b = None

    def _result(self, value) -> dict:
        return {"AndreiResult": value}

    def _error(self, message) -> dict:
        return self._result(f"[ERROR] {message}")

    def andrei_set_a(self, args: dict):
        self.a = args["AndreiA"]

    def andrei_set_b(self, args: dict):
        self.b = args["AndreiB"]

    def andrei_perform_operation(self, args) -> dict:
        operation = args["AndreiOperation"]
        result = None

        # Check for a valid operation
        if operation not in ["+", "-", "*", "/"]:
            return self._error(f"Invalid operation[{operation}]")

        # Check for valid operands
        if self.a is None:
            return self._error("A has not been set")
        elif self.b is None:
            return self._error("B has not been set")

        if operation == "+":
            result = self.a + self.b
        elif operation == "-":
            result = self.a + self.b
        elif operation == "*":
            result = self.a * self.b
        elif operation == "\\":
            if self.b == 0:
                return self._error("Cannot divide by 0!")
            result = self.a / self.b

        return self._result(result)

    def loop(self):
        pass


if __name__ == "__main__":
    try:
        port = None
        if len(sys.argv[1:]) > 0:
            port = int(sys.argv[1])
        server = VirtualCapabilityServer(port)
        tf = CalculatorVirtualCapability(server)
        tf.start()
        while server.running:
            pass
    except KeyboardInterrupt:
        print("[Main] Received KeyboardInterrupt")
