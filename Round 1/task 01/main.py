#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_data import GetData
from data_managment import DataManagment

__author__ = "Marius Wörfel"
__email__ = "raborogit@gmail.com"
__status__ = "Production"


def main() -> None:
    CARS_IN_SLOTS, CARS_IN_THE_WAY = GetData.get_and_return_data()
    data_managment = DataManagment(CARS_IN_SLOTS)
    CARS_NEED_MOVES = data_managment.select_cars_which_needs_moves(CARS_IN_SLOTS, CARS_IN_THE_WAY)
    data_managment.assign_moves_to_cars(CARS_IN_SLOTS, CARS_IN_THE_WAY, CARS_NEED_MOVES)


if __name__ == "__main__":
    main()