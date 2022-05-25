from itertools import takewhile

class GetData():

    @staticmethod
    def get_and_return_data():
        with open("files/parkplatz0.txt", "r") as file:
            data = file.read().split("\n")
        
        data.pop(-1)

        ALP = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        break_index = [index+1 for index, char in enumerate(ALP) if char == data[0][2]]
        cars_in_slots = [char for char in takewhile(lambda char: char != ALP[break_index[0]], ALP)]

        print(cars_in_slots)
