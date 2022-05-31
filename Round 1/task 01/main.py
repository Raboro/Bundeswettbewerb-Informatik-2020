#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_data import GetData
from solve_sliding_parking_lot import SolveSlidingParkingLot

__author__ = "Marius Wörfel"
__email__ = "raborogit@gmail.com"
__status__ = "Test 05/31/2022"


def main() -> None:
    CARS_IN_PARKSLOTS, BLOCKING_CARS = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz0.txt")
    solve_sliding_parking_lot = SolveSlidingParkingLot(CARS_IN_PARKSLOTS, BLOCKING_CARS)
    solve_sliding_parking_lot.assign_moves_to_cars()

    for car_and_result in solve_sliding_parking_lot.result:
        print(car_and_result)


if __name__ == "__main__":
    main()