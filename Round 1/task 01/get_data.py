from itertools import takewhile

class GetData():

    @staticmethod
    def get_data_from_file_return_necessary_data(file_path: str) -> list[str] and dict[str: list[int]]:
        """
        return CARS_IN_PARKSLOTS -> list of all cars in parkslots
        return BLOCKING_CARS -> dict of cars in the way of parkslots as keys and their positions in a list as their values
        e.g: A: [1, 2] => car A is in front of parkslot 2 and 3 (because counting starts at 0)
        """

        with open(file_path, "r") as file:
            data = file.read().split("\n")

        data.pop(-1)

        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        last_car = data[0][2]
        last_car_index = [index+1 for index, char in enumerate(alphabet) if char == last_car][0]

        #  add car to CARS_IN_PARKSLOTS as long it´s not the last car, if it´s the last car stop list comprehension 
        CARS_IN_PARKSLOTS = [car for car in takewhile(lambda car: car != alphabet[last_car_index], alphabet)]

        #  car: [position_1, position_2]
        BLOCKING_CARS = {cars[0]: [int(cars[1:]), int(cars[1:])+1] 
                            for cars in data[2:]}

        return CARS_IN_PARKSLOTS, BLOCKING_CARS