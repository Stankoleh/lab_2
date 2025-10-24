class Transport:
    def __init__(self, name, departure_date, arrival_date, direction):
        self.name = name
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.direction = direction
        self.__status = "scheduled"

    def delay(self, days):
        self.__status = "delayed"
        print(f"{self.name} transport delayed by {days} days.")

    def arrive(self):
        self.__status = "arrived"
        print(f"{self.name} has arrived successfully.")

    def get_status(self):
        return f"Transport: {self.name}, Status: {self.__status}"
