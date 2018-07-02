from rx import Observer


class NameObserver(Observer):

    def on_next(self, value):
        print("Received: {}".format(value))

    def on_completed(self):
        print("All names done!")

    def on_error(self, error):
        print("Error: {}".format(error))
