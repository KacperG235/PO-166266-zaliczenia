from vehicle import Vehicle


class Car(Vehicle):
    __price: float
    __colour: str
    __extra_seats: int

    def __init__(self, price: float = 0, colour: str = None, extra_seats: int = 0,
                 reg: str = None, model: int = 0, prod_year: int = 2022) -> None:
        if price < 0:
            self.__price = 0
        else:
            self.__price = price
        if extra_seats < 0:
            self.__extra_seats = 0
        else:
            self.__extra_seats = extra_seats
        self.__colour = colour
        super().__init__(reg, model, prod_year)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError('Wartosc nie spełnia założeń!')
        else:
            self.__price = value

    @property
    def colour(self) -> str:
        return self.__colour

    @colour.setter
    def colour(self, value: str) -> None:
        self.__colour = value

    @property
    def extra_seats(self) -> int:
        return self.__extra_seats

    @extra_seats.setter
    def extra_seats(self, value: int) -> None:
        if value < 0:
            raise ValueError('Wartosc nie spełnia założeń!')
        else:
            self.__extra_seats = value

    def drive(self) -> str:
        return f'Jadę świetnym pojazdem z roku {self.prod_year}! Ma kolor {self.colour}.'

    def __eq__(self, other) -> bool:
        return self.model == other.model and self.price == other.price

    def __ne__(self, other) -> bool:
        return self.model != other.model and self.price != other.price

    def __repr__(self) -> str:
        if self.reg is None:
            return f'Pojazd wyprodukowany w roku: {self.prod_year}.\nModel: {self.model}.\nCena: {self.price}.' \
                   f'\nKolor: {self.colour}.\nDodadkowe siedzenia: {self.extra_seats}.'
        else:
            return f'Pojazd wyprodukowany w roku: {self.prod_year}.\nModel: {self.model}.\nRejestracja: {self.reg}.' \
                   f'\nCena: {self.price}.\nKolor: {self.colour}.\nDodadkowe siedzenia: {self.extra_seats}.'
