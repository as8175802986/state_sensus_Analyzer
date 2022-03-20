from state_sensus_Analyzer.state_census_analyzer.state_code_analyzer import StateCodeAnalyser


class Test:
    @staticmethod
    def test_number_records_matches():

        try:
            result = StateCodeAnalyser.count_number_records()
            expected = 13
            if result==expected:
                return result

            else:
                raise (TypeError)
        except (TypeError):
            print("count not match")



    @staticmethod
    def test_check_file():
        try:
            result = StateCodeAnalyser.check_file()
            expected = "StateCensusData.csv"
            if result == expected:
                return result

            else:
                raise (TypeError)
        except (TypeError):
            print("invalid file")

    @staticmethod
    def test_check_file_extension():
        try:
            result = StateCodeAnalyser.check_file_extension()
            expected = ".csv"
            if result == expected:
                return result

            else:
                raise (TypeError)
        except (TypeError):
            print("invalid extension")

    @staticmethod
    def test_check_header():
        try:
            result = StateCodeAnalyser.check_header()
            expected = True
            if result == expected:
                return result

            else:
                raise (TypeError)
        except (TypeError):
            print("header not found ")

    @staticmethod
    def test_check_delimiter():
        try:
            result = StateCodeAnalyser.check_delimiter()
            expected = ','
            if result == expected:
                return result

            else:
                raise (TypeError)
        except (TypeError):
            print("incorrect delimiter found ")

if __name__ == '__main__':
    Test()
