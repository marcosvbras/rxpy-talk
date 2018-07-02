from rx import Observable
from observers import LanguageObserver


if __name__ == "__main__":

    languages = ["Python", "Ruby", "R", "Pascal", "Java", "JavaScript"]
    observable = Observable.from_(languages)

    observable.filter(
        lambda language: language.startswith("P")
    ).subscribe(LanguageObserver())
