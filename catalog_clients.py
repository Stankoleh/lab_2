from client import Client

class Catalog:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.clients = []
        return cls.instance

    def add_client(self, client: Client):
        if not any(c.passport == client.passport for c in self.clients):
            self.clients.append(client)
            print(f"Client {client.name} {client.surname} added to catalog.")
        else:
            print(f"Client with passport {client.passport} already exists!")

    def find_by_passport(self, passport):
        for c in self.clients:
            if c.passport == passport:
                return c
        print("Client not found.")
        return None

    def show_info(self):
        if not self.clients:
            print("No clients in catalog.")
        else:
            print("\n=== Client Catalog ===")
            for c in self.clients:
                print(f"{c.name} {c.surname} ({c.passport})")
