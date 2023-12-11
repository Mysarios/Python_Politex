from typing import Union


class Glass:
    def __init__(self, get_capacity_volume: Union[int, float], get_occupied_volume: Union[int, float]):

        if not isinstance(get_capacity_volume, (int, float)):
            raise TypeError
        if not get_capacity_volume > 0:
            raise ValueError
        self.capacity_volume = get_capacity_volume

        if not isinstance(get_occupied_volume, (int, float)):
            raise TypeError
        if get_occupied_volume < 0:
            raise ValueError
        self.occupied_volume = get_occupied_volume

    ...  # TODO инициализировать объект "Стакан"


if __name__ == "__main__":
    test1 = 50
    test2 = 5.5

    obj1 = Glass(test1,test2)  # Верные данные
    obj2 = Glass(test2,test1)  # некорректные данные
    # TODO попробовать инициализировать не корректные объекты