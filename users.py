from faker import Faker


def create_content(count: int) -> list:
    fake = Faker()
    content = [{'name': fake.name(), 'birthday': fake.date()}
               for _ in range(count)]
    return content
