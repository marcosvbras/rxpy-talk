from rx import Observer


class MovieObserver(Observer):
    """Listen and receive movies from an Observable object."""

    def on_next(self, value):
        print("Received: {}".format(value))

    def on_error(self, error):
        print("Error: {}".format(error))

    def on_completed(self):
        print("All movies done!")
