# dymmy data
# pip install faker
from faker import Faker

my_faker = Faker("ko_KR")
print(my_faker.name())
print(my_faker.address())
print(my_faker.phone_number())
print(my_faker.email())
print(my_faker.company())

for _ in range(5):
    print(my_faker.name(), my_faker.email())


for i in range(10):
    i += 1
    name = my_faker.name()
    email = my_faker.email()
    phone = my_faker.phone_number()
    print(
        f"insert into member(idx,name,email,phone) values({i}, '{name}','{email}','{phone}')"
    )

print(my_faker.name())
print(my_faker.address())
print(my_faker.postcode())
print(my_faker.country())
print(my_faker.job())
print(my_faker.user_name())
print(my_faker.catch_phrase())
print(my_faker.pyint(min_value=10, max_value=100))
