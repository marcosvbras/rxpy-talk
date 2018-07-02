from rx import Observer


class LanguageObserver(Observer):

    def on_next(self, value):
        print(value)

    def on_completed(self):
        print("All languages done!")

    def on_error(self, error):
        print("Error: {}".format(error))
