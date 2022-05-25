class DataManagment():

    def select_cars_which_needs_moves(self, CARS_IN_SLOTS: list[str], CARS_IN_THE_WAY: dict[str: list[int]]):
        return [car for index, car in enumerate(CARS_IN_SLOTS) for pos in CARS_IN_THE_WAY.values() if index in pos]