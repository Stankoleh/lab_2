from country import Country

class Residence:
    def __init__(self, country: Country, address, stars):
        self.country = country
        self.address = address
        self.stars = stars
        self._occupied = False

    def show_info(self):
        return f"{self.country.name}: {self.stars} residence at {self.address}"

    def check_in(self):
        if not self._occupied:
            self._occupied = True
            print(f"Guest checked into {self.address} ({self.stars})")
        else:
            print(f"{self.address} is currently occupied.")

    def check_out(self):
        if self._occupied:
            self._occupied = False
            print(f"Guest checked out from {self.address}")
        else:
            print(f"{self.address} is already free.")

