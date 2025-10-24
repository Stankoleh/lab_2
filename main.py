from datetime import date
from country import Country
from residence import Residence
from client import Client
from catalog_clients import Catalog
from transport import Transport
from journey import Journey

def main():
    country1 = Country("Italy", "Europe")
    residence1 = Residence(country1, "Via Roma 10", "4*")
    client1 = Client("Oleh", "Stanko", "AA123456", "+380501234567", "oleh@mail.com")
    transport1 = Transport("Plane", date(2025, 6, 5), date(2025, 6, 5), "forward")
    journey1 = Journey(
        country1, "Gran Via 22","5*","Plane", date(2025, 7, 10),date(2025, 7, 20),"forward")

    catalog1=Catalog()
    catalog1.add_client(client1)
    country1.update_rating(4.7)
    print(Country.get_total_countries())

    residence1.check_in()
    residence1.check_out()

    client1.insure()
    print(client1.get_contact_info())

    print(transport1.get_status())
    transport1.delay(2)
    transport1.arrive()

    journey1.calculate_price()
    print(catalog1.find_by_passport("AA123456"))

    print("\n")

    for obj in [country1, residence1, client1, journey1, catalog1]:
        if hasattr(obj, "show_info"):
            print(obj.show_info())

if __name__ == "__main__":
    main()
