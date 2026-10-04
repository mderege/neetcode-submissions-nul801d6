class Singleton:
    _uniqueInstance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._uniqueInstance == None:
            cls._uniqueInstance = super(Singleton, cls).__new__(cls)
        return cls._uniqueInstance

    

    def getValue(self) -> str:
        return self._val


    def setValue(self, value: str):
        self._val = value
