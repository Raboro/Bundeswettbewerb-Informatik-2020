#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_data import GetData
from solve_sliding_parking_lot import SolveSlidingParkingLot

__author__ = "Marius Wörfel"
__email__ = "raborogit@gmail.com"
__status__ = "Refactoring 05/30/2022"


def main() -> None:
    CARS_IN_PARKSLOTS, BLOCKING_CARS = GetData.get_data_from_file_return_necessary_data()
    solve_sliding_parking_lot = SolveSlidingParkingLot(CARS_IN_PARKSLOTS, BLOCKING_CARS)
    solve_sliding_parking_lot.assign_moves_to_cars()

    for car_and_result in solve_sliding_parking_lot.result:
        print(car_and_result)


if __name__ == "__main__":
    main()