class Book:
    def __init__(self, nameBook: str, nameAuthor: str, countPages: int):
        self._name = name
        self._author = author
        self._countPages = countPages
    @property
    def nameBook(self):
        return self._name
    @property
    def nameAuthor(self):
        return self._author

    def __str__(self):
        return f"Название книги = {self.nameBook}. Имя Автора = {self.nameAuthor}. Количество страниц в книге ={self.countPages}."
    def __repr__(self):
        return f"{self.__class__.__name__}(nameBook={self.nameBook!r}, author={self.nameAuthor!r}, countPages={self.countPages})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int, weight: int):
        super().__init__(name, author,pages)
        self._weight = weight

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, countPages={self.countPages}, weight ={self.weight})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, pages: int, weightMB: float):
        super().__init__(name, author,pages)
        self._weightMB = weightMB

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._duration}, MB ={self.weightMB})"
