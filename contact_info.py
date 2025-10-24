class ContactInfo:
    def __init__(self, phone, email):
        self.phone = phone
        self.email = email

    def get_contact_info(self):
        return f"Phone: {self.phone}, Email: {self.email}"
