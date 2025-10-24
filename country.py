class Country:
    total_countries = 0

    def __init__(self, name, continent):
        self.name = name
        self.continent = continent
        self._active = True
        self.__rating = 5.0
        Country.total_countries += 1

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        self._active = value

    def deactivate(self):
        self._active = False
        print(f"Country {self.name} is temporarily unavailable for travel.")

    def show_info(self):
        print(f"{self.name} (Continent: {self.continent}, Rating: {self.__rating}/5)")

    def update_rating(self, new_rating):
        if 0 <= new_rating <= 5:
            self.__rating = new_rating
            print(f"Country {self.name} rating updated to {self.__rating}/5")
        else:
            print("Invalid rating value!")

    @staticmethod
    def get_total_countries():
        return f"Total countries registered: {Country.total_countries}"
