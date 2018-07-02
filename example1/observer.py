from rx import Observer

class MovieObserver(Observer):

    def on_next(self, value):
        print("Received: {}".format(value))

    def on_error(self, error):
        print("Error: {}".format(error))

    def on_completed(self):
        print("Completed")
