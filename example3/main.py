from rx import Observable
from observers import NameObserver


if __name__ == '__main__':

    names = ["Hikari", "Ayame", "Hyuga", "Sakura", "Akira", "Hideyo"]
    observable = Observable.from_(names)
    observable.filter(
        lambda name: name.startswith("A")
    ).map(
        lambda name: name.upper()
    ).subscribe(NameObserver())
