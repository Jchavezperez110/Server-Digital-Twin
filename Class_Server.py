# A cyber security company is testing a digital twin of a server.


class server:
    """Represent a server's digital-twin state and operations."""

    def __init__(self, hostname):
        self.hostname = hostname
        self.status = "OFF"
        self.CPU_USAGE = 0

    def BOOT(self):
        self.status = "ON"
        print(f"{self.hostname} is booting up.")

    def SHUTDOWN(self):
        self.status = "OFF"
        print(f"{self.hostname} is shutting down.")

    def INCREASE_LOAD(self, load):
        if self.status == "ON":
            self.CPU_USAGE += load
            print(
                f"{self.hostname} CPU usage increased by {load}%. "
                f"Current CPU usage: {self.CPU_USAGE}%"
            )
        else:
            print(f"{self.hostname} is OFF. Cannot increase load.")

    def DISPLAY_STATUS(self):
        print(
            f"Hostname: {self.hostname}, Status: {self.status}, "
            f"CPU Usage: {self.CPU_USAGE}%"
        )


if __name__ == "__main__":
    digital_twin = server("server-01")
    digital_twin.BOOT()
    digital_twin.INCREASE_LOAD(25)
    digital_twin.DISPLAY_STATUS()
    digital_twin.SHUTDOWN()
    digital_twin.DISPLAY_STATUS()
