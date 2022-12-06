class Vehicle:
    __reg: str
    __model: int
    __prod_year: int

    def __init__(self, reg: str = None, model: int = 0, prod_year: int = 2022) -> None:
        self.__reg = reg
        if model < 0:
            self.__model = 0
        else:
            self.__model = model
        if 1900 > prod_year > 2022:
            self.__prod_year = 2022
        else:
            self.__prod_year = prod_year

    @property
    def reg(self) -> str:
        return self.__reg

    @reg.setter
    def reg(self, value: str) -> None:
        self.__reg = value

    @property
    def model(self) -> int:
        return self.__model

    @model.setter
    def model(self, value: int) -> None:
        if value < 0:
            raise ValueError('Wartosc nie spełnia założeń!')
        else:
            self.__model = value

    @property
    def prod_year(self) -> int:
        return self.__prod_year

    @prod_year.setter
    def prod_year(self, value: int) -> None:
        if 1900 > value > 2022:
            raise ValueError('Wartosc nie spełnia zalozen!')
        else:
            self.__prod_year = value

    def brake(self) -> str:
        return 'Zatrzymaj się'

    def drive(self) -> str:
        return f'Jadę świetnym pojazdem z roku {self.prod_year}!'

    def __repr__(self) -> str:
        if self.reg is None:
            return f'Pojazd wyprodukowany w roku: {self.prod_year}.\nModel: {self.model}.'
        else:
            return f'Pojazd wyprodukowany w roku: {self.prod_year}.\nModel: {self.model}.\nRejestracja: {self.reg}.'

    def __eq__(self, other) -> bool:
        if self.model == other.model:
            return self.prod_year == other.prod_year
        else:
            return self.model == other.model

    def __ne__(self, other) -> bool:
        if self.model != other.model:
            return self.prod_year == other.prod_year
        else:
            return self.model != other.model
