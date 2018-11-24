
class User:
    def __init__(self, con):
        self.c = con

    def json(self):
        return {'age': self.age, 'name': self.name}

    def getById(self, _value):
        self.c.execute('SELECT * from users WHERE id=?', (_value))
        self.name , self.age = self.c.fetch()

        return self.json()

    def post(self, name, age):
        self.c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))

        return 1
