class User:
    def __init__(
        self,
        first_name,
        last_name,
        age,
        email,
        city,
        occupation,
        interests,
        is_active=True,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        self.occupation = occupation
        self.interests = interests
        self.is_active = is_active

    def describe_user(self):
        print("User Profile Summary")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"City: {self.city}")
        print(f"Occupation: {self.occupation}")
        print(f"Interests: {', '.join(self.interests)}")
        print(f"Account Active: {'Yes' if self.is_active else 'No'}")

    def greet_user(self):
        print(
            f"Hello, {self.first_name}! Welcome back."
            f" We hope you enjoy your time in {self.city}."
        )


# Create two different user instances and call both methods for each user.
user_one = User(
    first_name="Bradley",
    last_name="Robinson",
    age=28,
    email="bradley.robinson@example.com",
    city="Seattle",
    occupation="Data Analyst",
    interests=["reading", "hiking", "photography"],
)

user_two = User(
    first_name="Noah",
    last_name="Burkin",
    age=35,
    email="noah.burkin@example.com",
    city="Austin",
    occupation="Software Engineer",
    interests=["gaming", "travel", "cooking"],
    is_active=False,
)

for user in (user_one, user_two):
    user.describe_user()
    user.greet_user()
    print("-" * 40)


print("\nMultilevel Inheritance Example")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Mammal(Animal):
    def walk(self):
        print(f"{self.name} is walking.")


class Dog(Mammal):
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")


pet = Dog("Buddy")
pet.eat()   # Inherited from Animal
pet.walk()  # Inherited from Mammal
pet.bark()  # Defined in Dog
