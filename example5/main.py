from rx import Observable
from pymongo import MongoClient
from rx.concurrency.newthreadscheduler import Scheduler, Disposable

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost')
    movies = client.cinema.movies

    Observable.from_(movies.find().limit(10)) \
        .subscribe_on(Scheduler.new_thread) \
        .subscribe(lambda d: print(d['title']))
