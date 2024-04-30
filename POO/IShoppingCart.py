from abc import ABCMeta, abstractmethod


class IShoppingCart(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod 
    def edit(self):
        pass
     
    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def checkout(self):
        pass
    