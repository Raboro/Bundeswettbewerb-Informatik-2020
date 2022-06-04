import time
from get_data import GetData
from solve_sliding_parking_lot import SolveSlidingParkingLot


class TestSolveSlidingParkingLot():

    def __init__(self) -> None:
        self.start_time = time.time()

        self.test_counter = 30
        self.passed_tests = 0
        self.failed_tests = 0
        self.test_result = 0

        self.start_tests()
        result = self.get_test_result()
        print(f"\033[97mResult: {result:.0%}\nTest passed: {self.passed_tests}\nTest failed {self.failed_tests}\033[97m")
        print(f"\n--- {time.time() - self.start_time} seconds executing time ---")


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
        self.solve_sliding_parking_lot_test_assign_moves_to_cars_one_car_gets_blocked_04()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_right_move_01()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_right_move_02()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_right_move_03()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_left_move_01()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_left_move_02()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_left_move_03()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_one_multiple_move_01()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_one_multiple_move_02()
        self.solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_one_multiple_move_03()
        self.solve_sliding_parking_lot_test_one_move_get_blocking_car_blocking_car()
        self.solve_sliding_parking_lot_test_get_moves_needed_per_side_1_left_2_right()
        self.solve_sliding_parking_lot_test_get_moves_needed_per_side_2_left_1_right()
        self.solve_sliding_parking_lot_test_find_range_of_blocking_cars_and_side_left_01()
        self.solve_sliding_parking_lot_test_find_range_of_blocking_cars_and_side_left_02()
        self.solve_sliding_parking_lot_test_find_range_of_blocking_cars_and_side_right_01()
        self.solve_sliding_parking_lot_test_find_range_of_blocking_cars_and_side_right_02()
        self.solve_sliding_parking_lot_test_get_multiple_cars_need_to_move_one_car_two_moves()
        self.solve_sliding_parking_lot_test_get_multiple_cars_need_to_move_two_cars_both_two_moves()
        self.solve_sliding_parking_lot_test_get_multiple_cars_need_move_one_car_two_moves()


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


    def solve_sliding_parking_lot_test_assign_moves_to_cars_one_car_gets_blocked_04(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "P", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AP", "AX", "AY", "AZ"], BLOCKING_CARS={"BA": [51, 52]})
        test_obj.assign_moves_to_cars()
        self.check_if_equal(test_result=test_obj.result, result=['A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'P:', 'X:', 'Y:', 'Z:', 'AA:', 'AB:', 'AC:', 'AD:', 'AE:', 'AF:', 'AG:', 'AH:', 'AI:', 'AJ:', 'AK:', 'AL:', 'AM:', 'AN:', 'AO:', 'AP:', 'AQ:', 'AR:', 'AS:', 'AT:', 'AU:', 'AV:', 'AP:', 'AX:', 'AY:', 'AZ: BA 2 left'], test_num=11)


    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_right_move_01(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [0, 1]})
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="right", test_num=12)
    

    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_right_move_02(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [1, 2]})
        test_obj.car_position = 1
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="right", test_num=13)

    
    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_right_move_03(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [2, 3]})
        test_obj.car_position = 2
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="right", test_num=14)

    
    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_left_move_01(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [3, 4]})
        test_obj.car_position = 4
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="left", test_num=15)
    

    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_left_move_02(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [2, 3]})
        test_obj.car_position = 3
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="left", test_num=16)

    
    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_single_left_move_03(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [1, 2]})
        test_obj.car_position = 2
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="left", test_num=17)

    
    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_one_multiple_move_01(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [0, 1], "G": [2, 3]})
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="multiple", test_num=18)
    

    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_one_multiple_move_02(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [1, 2], "G": [3, 4]})
        test_obj.car_position = 3
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="multiple", test_num=19)


    def solve_sliding_parking_lot_test_check_if_car_needs_one_or_multiple_moves_one_multiple_move_03(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [1, 2], "G": [3, 4]})
        test_obj.car_position = 4
        test_result = test_obj.check_if_car_needs_one_or_multiple_moves()
        self.check_if_equal(test_result=test_result, result="multiple", test_num=20)


    def solve_sliding_parking_lot_test_one_move_get_blocking_car_blocking_car(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E"], BLOCKING_CARS={"F": [0, 1]})
        test_result = test_obj.one_move_get_blocking_car()
        self.check_if_equal(test_result=test_result, result="F", test_num=21)


    def solve_sliding_parking_lot_test_get_moves_needed_per_side_1_left_2_right(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F", "G", "H"], BLOCKING_CARS={"I": [1, 2], "J": [3, 4], "K": [5, 6]})
        test_obj.car_position = 2
        test_result = test_obj.get_moves_needed_per_side()
        self.check_if_equal(test_result=test_result, result=[[1, 2], [1, 2]], test_num=22)


    def solve_sliding_parking_lot_test_get_moves_needed_per_side_2_left_1_right(self) -> None:
        test_obj = SolveSlidingParkingLot(["A", "B", "C", "D", "E", "F", "G", "H"], BLOCKING_CARS={"I": [1, 2], "J": [3, 4], "K": [5, 6]})
        test_obj.car_position = 1
        test_result = test_obj.get_moves_needed_per_side()
        self.check_if_equal(test_result=test_result, result=[[2, 1], [2, 1]], test_num=23)


    def solve_sliding_parking_lot_test_find_range_of_blocking_cars_and_side_left_01(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F", "G", "H"], BLOCKING_CARS={"I": [1, 2], "J": [3, 4], "K": [5, 6]})
        test_obj.car_position = 2
        test_result = test_obj.find_range_of_blocking_cars_and_side(moves_needed_per_side=[1, 2], backup_moves_needed_per_side=[1,2])
        self.check_if_equal(test_result=test_result, result=[-1, 'left', 1], test_num=24)

    
    def solve_sliding_parking_lot_test_find_range_of_blocking_cars_and_side_left_02(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F", "G", "H"], BLOCKING_CARS={"I": [3, 4], "J": [5, 6]})
        test_obj.car_position = 5
        test_result = test_obj.find_range_of_blocking_cars_and_side(moves_needed_per_side=[1, 2], backup_moves_needed_per_side=[1, 2])
        self.check_if_equal(test_result=test_result, result=[1, 'left', 1], test_num=25)


    def solve_sliding_parking_lot_test_find_range_of_blocking_cars_and_side_right_01(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F", "G", "H"], BLOCKING_CARS={"I": [3, 4], "J": [5, 6]})
        test_obj.car_position = 5
        test_result = test_obj.find_range_of_blocking_cars_and_side(moves_needed_per_side=[2, 1], backup_moves_needed_per_side=[2,1])
        self.check_if_equal(test_result=test_result, result=[8, 'right', 1], test_num=26)


    def solve_sliding_parking_lot_test_find_range_of_blocking_cars_and_side_right_02(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F", "G", "H"], BLOCKING_CARS={"I": [0, 1], "J": [2, 3], "K": [4, 5]})
        test_obj.car_position = 4
        test_result = test_obj.find_range_of_blocking_cars_and_side(moves_needed_per_side=[1, 2], backup_moves_needed_per_side=[1, 2])
        self.check_if_equal(test_result=test_result, result=[8, 'right', 2], test_num=27)


    def solve_sliding_parking_lot_test_get_multiple_cars_need_to_move_one_car_two_moves(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F"], BLOCKING_CARS={"G": [4, 5]})
        test_obj.car_position = 5
        test_result = test_obj.get_multiple_cars_need_to_move([3, "left", 1])
        self.check_if_equal(test_result=test_result, result="G 1 left", test_num=28)


    def solve_sliding_parking_lot_test_get_multiple_cars_need_to_move_two_cars_both_two_moves(self) -> None:
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F"], BLOCKING_CARS={"G": [4, 5], "H": [2, 3]})
        test_obj.car_position = 4
        test_result = test_obj.get_multiple_cars_need_to_move([1, "left", 2])
        self.check_if_equal(test_result=test_result, result= "H 2 left, G 2 left", test_num=29)


    def solve_sliding_parking_lot_test_get_multiple_cars_need_move_one_car_two_moves(self) -> None: 
        test_obj = SolveSlidingParkingLot(CARS_IN_PARKSLOTS=["A", "B", "C", "D", "E", "F"], BLOCKING_CARS={"G": [0, 1], "H": [2, 3]})
        test_obj.car_position = 2
        test_result = test_obj.get_multiple_cars_need_to_move([2, "right", 2])
        self.check_if_equal(test_result=test_result, result="H 2 right", test_num=30)

    def get_test_result(self) -> float:
        return self.passed_tests / self.test_counter


if __name__ == "__main__":
    TestSolveSlidingParkingLot()