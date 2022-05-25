#!/usr/bin/env python
# -*- coding: utf-8 -*-

from get_data import GetData

__author__ = "Marius Wörfel"
__email__ = "raborogit@gmail.com"
__status__ = "Production"


def main() -> None:
    CARS_IN_SLOTS, CARS_IN_THE_WAY = GetData.get_and_return_data()


if __name__ == "__main__":
    main()