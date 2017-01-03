from dog import Dog

class Poodle(Dog):
    def __init__(self, hair):
        self.hair = hair

    def get_hair(self):
        return self.hair