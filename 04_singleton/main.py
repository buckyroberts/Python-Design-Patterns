class Singleton(object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('Instance does not exist...')
        else:
            print('Instance exists:', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

a = Singleton()

# Once a singleton is created, all instances of this class will use the same object
print('Creating instance', Singleton.get_instance())

# Since singleton already created, the existing object is returned
b = Singleton()

# Even though we now have 3 different instances of this class, they all reference the same object
c = Singleton()
