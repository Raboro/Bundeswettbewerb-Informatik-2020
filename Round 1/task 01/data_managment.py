class DataManagment():
    
    def __init__(self, CARS_IN_SLOTS) -> None:
        self.result = []
        self.LENGTH_PARKSLOT = len(CARS_IN_SLOTS)
        

    def select_cars_which_needs_moves(self, CARS_IN_SLOTS: list[str], CARS_IN_THE_WAY: dict[str: list[int]]) -> list[str]:
        """
        return a list of cars, which are blocked and can`t get our directly
        """
        
        return [car for index_car, car in enumerate(CARS_IN_SLOTS) for positions in CARS_IN_THE_WAY.values() if index_car in positions]

    
    def assign_moves_to_cars(self, CARS_IN_SLOTS: list[str], CARS_IN_THE_WAY: dict[str: list[int]], CARS_NEED_MOVES: list[str]) -> list[str]:
        """
        assign each car to moves, which are needed, that the car can move out of the slot
        e.g A: B 1 right => For car A, car B needs to be moves one time to the right
        return the result in a list
        """

        for car in CARS_NEED_MOVES:
            pre_pos = [index for index, value in enumerate(CARS_IN_SLOTS) if value == car]
            position_car = pre_pos[0]
            
            move_status = self.check_if_car_needs_one_or_multiple_moves(position_car, CARS_IN_THE_WAY)
            print(move_status)


    def check_if_car_needs_one_or_multiple_moves(self, position_car: int, CARS_IN_THE_WAY: dict[str: list[int]]) -> list[int, str]:
        """
        return if the selected car, needs multiple car moves to come out, if not return the direction the blocking car needs to be moved
        """

        blocking_car_positions = [position for positions in CARS_IN_THE_WAY.values() for position in positions]

        if position_car + 1 in blocking_car_positions and position_car + 2 not in blocking_car_positions and position_car + 2 < self.LENGTH_PARKSLOT:
            return [1, "right"]
        
        elif position_car - 1 in blocking_car_positions and position_car - 2 not in blocking_car_positions and position_car + 2 >= 0:
            return [1, "left"]
        
        return [0, "multiple"]
             