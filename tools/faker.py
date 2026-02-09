from faker import Faker


class Fake:

    def __init__(self, faker: Faker):

        self.faker = faker

    def last_name(self) -> str:

        return self.faker.last_name()

    def first_name(self) -> str:

        return self.faker.first_name()

    def postal_code(self) -> str:

        return self.faker.postcode()

fake = Fake(faker=Faker())