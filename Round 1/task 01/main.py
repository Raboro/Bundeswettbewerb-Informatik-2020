#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_data import GetData
from data_managment import DataManagment

__author__ = "Marius Wörfel"
__email__ = "raborogit@gmail.com"
__status__ = "Production"


def main() -> None:
    CARS_IN_SLOTS, CARS_IN_THE_WAY = GetData.get_and_return_data()
    dm = DataManagment()
    cars_need_moves = dm.select_cars_which_needs_moves(CARS_IN_SLOTS, CARS_IN_THE_WAY)
    print(cars_need_moves)


if __name__ == "__main__":
    main()