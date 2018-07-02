from rx import Observable
from observer import MovieObserver

if __name__ == '__main__':

    movies = [
        "Star Wars", "Pirates of the Caribbean", "Back to the Future",
        "Sherlock Holmes", "The Martian", "Interestelar", "Jurassic Park"
    ]

    observable = Observable.from_(movies)

    observable.subscribe(MovieObserver())
