'''
Implement the singleton pattern with a twist. First, instead of storing one instance,
store two instances. And in every even call of getInstance(), return the first instance
and in every odd call of getInstance(), return the second instance.
'''

from __future__ import annotations

class Twisted_Singleton:

    _instance1 = None
    _instance2 = None
    _isInitialized = False

    def __init__(self, instance_num: int) -> None:
        self.instance_num = instance_num

    def __repr__(self) -> str:
        return str(self.instance_num)
    
    @staticmethod
    def initialize() -> None:

        if not Twisted_Singleton._isInitialized:

            Twisted_Singleton._instance1 = Twisted_Singleton(1)
            Twisted_Singleton._instance2 = Twisted_Singleton(2)
            Twisted_Singleton._is_initialized = True
    
    @staticmethod
    def getInstance() -> Twisted_Singleton