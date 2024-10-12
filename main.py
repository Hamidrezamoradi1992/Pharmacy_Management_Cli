import atexit
import signal

from models import User, Access, Drug,Sale_Drug,Menu_Access
from routes import router
from core.db import DataBase
from core.hook import Hook, Mode
from core.lifecycle import LifeCycle

if __name__ == '__main__':
    # Database
    db = DataBase("db.pickle")
    db.register(User)
    db.register(Access)
    db.register(Drug)
    db.register(Sale_Drug)
    db.register(Menu_Access)

    # Intercept
    atexit.register(db.save)
    signal.signal(signal.SIGTERM, lambda signum, frame: exit())

    # Hooks
    Hook(Mode.INITIAL, db.load)
    Hook(Mode.FINISH, lambda: db.save() or atexit.unregister(db.save))

    # Lifecycle
    with LifeCycle() as lifecycle:
        router()

