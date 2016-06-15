class Publisher(object):
    users = set()

    def register(self, user):
        self.users.add(user)

    def unregister(self, user):
        self.users.discard(user)

    def send_notifications(self, message):
        for user in self.users:
            user.notify(message)


class Subscriber(object):

    def __init__(self, username):
        self.username = username

    def notify(self, message):
        print(self.username + ' received message: ' + message)

publisher = Publisher()

# Create observers that will receive notifications
bucky = Subscriber('Bucky')
sally = Subscriber('Sally')
publisher.register(bucky)
publisher.register(sally)

# Notifications are sent to every observer (subscriber)
publisher.send_notifications('We updated the website')
publisher.send_notifications('Make sure to add a profile picture')
