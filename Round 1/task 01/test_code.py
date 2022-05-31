from get_data import GetData
from solve_sliding_parking_lot import SolveSlidingParkingLot

class TestSolveSlidingParkingLot():

    def __init__(self) -> None:
        self.test_counter = 6
        self.passed_tests = 0
        self.failed_tests = 0
        self.test_result = 0
        self.start_tests()
        result = self.get_test_result()
        print(result)

        


    def start_tests(self):
        self.test_input_file_0()
        self.test_input_file_1()
        self.test_input_file_2()
        self.test_input_file_3()
        self.test_input_file_4()
        self.test_input_file_5()


    def check_if_Equal(self, test_result, result, test_num):
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
                

    def test_input_file_0(self):
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz0.txt")
        self.check_if_Equal(test_result=test_result, result=(['A', 'A', 'C', 'D', 'E', 'F', 'G'], {'H': [2, 3], 'I': [5, 6]}), test_num=1)
    

    def test_input_file_1(self):
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz1.txt")
        self.check_if_Equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'], {'O': [1, 2], 'P': [3, 4], 'Q': [6, 7], 'R': [10, 11]}), test_num=2)


    def test_input_file_2(self):
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz2.txt")
        self.check_if_Equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'], {'O': [2, 3], 'P': [5, 6], 'Q': [7, 8], 'R': [9, 10], 'S': [12, 13]}), test_num=3)


    def test_input_file_3(self):
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz3.txt")
        self.check_if_Equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'], {'O': [1, 2], 'P': [4, 5], 'Q': [8, 9], 'R': [10, 11], 'S': [12, 13]}), test_num=4)


    def test_input_file_4(self):
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz4.txt")
        self.check_if_Equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'], {'Q': [0, 1], 'R': [2, 3], 'S': [6, 7], 'T': [10, 11], 'U': [13, 14]}), test_num=5)


    def test_input_file_5(self):
        test_result = GetData.get_data_from_file_return_necessary_data(file_path="/home/marius/Documents/Bundeswettbewerb Informatik 2021/Round 1/task 01/files/parkplatz5.txt")
        self.check_if_Equal(test_result=test_result, result=(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'], {'P': [2, 3], 'Q': [4, 5], 'R': [8, 9], 'S': [12, 13]}), test_num=6)


    def get_test_result(self):
        return 100 * float(self.test_counter) / float(self.failed_tests) if self.failed_tests > 0 else 100.00

if __name__ == "__main__":
    TestSolveSlidingParkingLot()