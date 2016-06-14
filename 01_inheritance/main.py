class Enemy(object):

    def move_left(self):
        print('Moving left...')

    def move_right(self):
        print('Moving left...')


class Ninja(Enemy):

    def karate_chop(self):
        print('Karate chop!')


class Zombie(Enemy):

    def bite(self):
        print('I am biting you!')


enemy = Enemy()
enemy.move_left()

# Ninja also includes all functions from parent class (Enemy)
ninja = Ninja()
ninja.move_left()
ninja.karate_chop()

# Zombie is called the (child class), inherits from Enemy (parent class)
zombie = Zombie()
zombie.move_right()
zombie.bite()
