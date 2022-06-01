import time
from get_data import GetData
from solve_sliding_parking_lot import SolveSlidingParkingLot


class TestSolveSlidingParkingLot():

    def __init__(self) -> None:
        self.start_time = time.time()

        self.test_counter = 10
        self.passed_tests = 0
        self.failed_tests = 0
        self.test_result = 0

        self.start_tests()
        result = self.get_test_result()
        print(f"\033[97mResult: {result:.0%}\nTest passed: {self.passed_tests}\nTest failed {self.failed_tests}\033[97m")
        print("\n--- %s seconds executing time---" % (time.time() - self.start_time))


    def start_tests(self) -> None:
        #  GetData
        self.get_data_test_input_file_0()
        self.get_data_test_input_file_1()
        self.get_data_test_input_file_2()
        self.get_data_test_input_file_3()
        self.get_data_test_input_file_4()
        self.get_data_test_input_file_5()

        #  SolveSlidingParking_lot
        self.solve_sliding_parking_lot_test_assign_moves_to_cars_no_blocking_car()
        self.solve_sliding_parking_lot_test_assign_moves_to_cars_one_car_gets_blocked_01()
        self.solve_sliding_parking_lot_test_assign_moves_to_cars_one_car_gets_blocked_02()
        self.solve_sliding_parking_lot_test_assign_moves_to_cars_one_car_gets_blocked_03()


    def check_if_equal(self, test_result, result, test_num) -> None:
        if test_result == result:
            self.passed_tests += 1
            if test_num < 10:
                print("\033[92m=================================\033[92m") 
                print(f"\033[92m========= Test {test_num} passed =========\033[92m") 
                print("\033[92m=================================\033[92m\n") 
            
            else:
                print("\033[92m=================================\033[92m") 
                print(f"\033[92m======== Test {test_num} passed =========\033[92m") 
                print("\033[92m=================================\033[92m\n") 

        else:
            self.failed_tests += 1
            if test_num < 10:
                print("\033[91m=================================\033[91m") 
                print(f"\033[91m========= Test {test_num} failed =========\033[91m") 
                print("\033[91m=================================\033[91m\n") 
            
            else:
                print("\033[91m=================================\033[91m") 
                print(f"\033[91m======== Test {test_num} failed =========\033[91m") 
                print("\033[91m=================================\033[91m\n") 

            print(f"\033[91mYour result: {test_result}\033[91m")
            print(f"\033[92mCorrect result: {result}\033[92m\n")
                

    #  GetData tests
    def get_data_test_input_file_0(self) -> None:
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz0.txt")
        self.check_if_equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G'], {'H': [2, 3], 'I': [5, 6]}), test_num=1)
    

    def get_data_test_input_file_1(self) -> None:
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz1.txt")
        self.check_if_equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'], {'O': [1, 2], 'P': [3, 4], 'Q': [6, 7], 'R': [10, 11]}), test_num=2)


    def get_data_test_input_file_2(self) -> None:
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz2.txt")
        self.check_if_equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'], {'O': [2, 3], 'P': [5, 6], 'Q': [7, 8], 'R': [9, 10], 'S': [12, 13]}), test_num=3)


    def get_data_test_input_file_3(self) -> None:
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz3.txt")
        self.check_if_equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'], {'O': [1, 2], 'P': [4, 5], 'Q': [8, 9], 'R': [10, 11], 'S': [12, 13]}), test_num=4)


    def get_data_test_input_file_4(self) -> None:
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz4.txt")
        self.check_if_equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'], {'Q': [0, 1], 'R': [2, 3], 'S': [6, 7], 'T': [10, 11], 'U': [13, 14]}), test_num=5)


    def get_data_test_input_file_5(self) -> None:
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz5.txt")
        self.check_if_equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'], {'P': [2, 3], 'Q': [4, 5], 'R': [8, 9], 'S': [12, 13]}), test_num=6)


    # SolveSlidingParkingLot tests
    def solve_sliding_parking_lot_test_assign_moves_to_cars_no_blocking_car(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D"], BLOCKING_CARS={})
        test_obj.assign_moves_to_cars()
        self.check_if_equal(test_result=test_obj.result, result=['A:', 'B:', 'C:', 'D:'], test_num=7)


    def solve_sliding_parking_lot_test_assign_moves_to_cars_one_car_gets_blocked_01(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D"], BLOCKING_CARS={"E": [3, 4]})
        test_obj.assign_moves_to_cars()
        self.check_if_equal(test_result=test_obj.result, result=['A:', 'B:', 'C:', 'D: E 2 left'], test_num=8)


    def solve_sliding_parking_lot_test_assign_moves_to_cars_one_car_gets_blocked_02(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"], BLOCKING_CARS={"Q": [15, 16]})
        test_obj.assign_moves_to_cars()
        self.check_if_equal(test_result=test_obj.result, result=['A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P: Q 2 left'], test_num=9)


    def solve_sliding_parking_lot_test_assign_moves_to_cars_one_car_gets_blocked_03(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "P", "X", "Y", "Z"], BLOCKING_CARS={"Ü": [25, 26]})
        test_obj.assign_moves_to_cars()
        self.check_if_equal(test_result=test_obj.result, result=['A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'P:', 'X:', 'Y:', 'Z: Ü 2 left'], test_num=10)



    def get_test_result(self) -> float:
        return self.passed_tests / self.test_counter


if __name__ == "__main__":
    TestSolveSlidingParkingLot()