from faker import Faker

fake = Faker()

for i in range(10):
    fakeName = fake.name()
    fakeEmail = fake.email()
    fakePhone = fake.phone_number()

    print(f"Name: {fakeName}")
    print(f"Email: {fakeEmail}")
    print(f"Phone Number: {fakePhone}")
    print("                          ")