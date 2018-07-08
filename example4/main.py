from rx import Observable


if __name__ == '__main__':

    Observable.from_(range(10)) \
        .filter(lambda number: number % 2 == 1) \
        .map(lambda number: number + 2) \
        .subscribe(
            on_next=lambda number: print(number),
            on_completed=lambda: print("All numbers done!"),
            on_error=lambda error: print(error)
        )

    Observable.from_(range(10)) \
        .subscribe(
            lambda value: print(value),
            lambda error: print(error)
        )
