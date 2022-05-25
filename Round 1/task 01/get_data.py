from itertools import takewhile

class GetData():

    @staticmethod
    def get_and_return_data() -> list[str] and dict[str: list[int]]:
        """
        create CARS_IN_SLOTS -> list of all cars in parkslots
        create CARS_IN_THE_WAY -> dict of cars in the way of parkslots and their positions in a list 
            e.g: A: [1, 2] => car A is in front of parkslot 2 and 3 (because counting starts at 0)
        """

        with open("files/parkplatz1.txt", "r") as file:
            data = file.read().split("\n")

        data.pop(-1)

        ALP = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        break_index = [index+1 for index, char in enumerate(ALP) if char == data[0][2]]
        CARS_IN_SLOTS = [char for char in takewhile(lambda char: char != ALP[break_index[0]], ALP)]

        CARS_IN_THE_WAY = {cars[0]: [int(cars[1:]), int(cars[1:])+1] for cars in data[2:]}

        return CARS_IN_SLOTS, CARS_IN_THE_WAY