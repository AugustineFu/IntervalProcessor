import random
import sys
from faker import Faker
# from basic_table import db, User, app
from editable_table import db, User, app


def create_fake_users(n):
    """Generate fake users."""
    with app.app_context():
        db.session.add(User("Name","age","Minimal","Maximal","Email"))
        db.session.commit()
    faker = Faker()
    for i in range(n):
        user = User(faker.name(),
                    str(random.randint(20, 80)),
                    str(random.uniform(2.1, 50.4)),
                    # faker.address().replace('\n', ', '),
                    str(random.uniform(50.5, 85.5)),
                    faker.email())
        with app.app_context():
            db.session.add(user)
            db.session.commit()
    with app.app_context():
        users = User.query.all()
        print(users)
    print(f'Added {n} fake users to the database.')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('Pass the number of users you want to create as an argument.')
        sys.exit(1)
    create_fake_users(int(sys.argv[1]))
