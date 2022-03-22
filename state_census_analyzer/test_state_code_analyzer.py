from state_sensus_Analyzer.state_census_analyzer.state_code_analyzer import StateCodeAnalyser


class Test:
    @staticmethod
    def test_number_records_matches():
        result = StateCodeAnalyser.count_number_records()
        expected = 11
        assert (result == expected)

    @staticmethod
    def test_number_records_not_matches():
        result = StateCodeAnalyser.count_number_records()
        expected = 12
        assert (result != expected)

    @staticmethod
    def test_check_file():
        result = StateCodeAnalyser.check_file()
        expected = "state_code.csv"
        assert (result == expected)

    @staticmethod
    def test_check_file_not_valid():
        result = StateCodeAnalyser.check_file()
        expected = "State_code.csv"
        assert (result != expected)

    @staticmethod
    def test_check_file_extension():
        result = StateCodeAnalyser.check_file_extension()
        expected = ".csv"
        assert (result == expected)

    @staticmethod
    def test_check_file_extension_not_valid():
        result = StateCodeAnalyser.check_file_extension()
        expected = ".cs"
        assert (result != expected)

    @staticmethod
    def test_check_header():
        result = StateCodeAnalyser.check_header()
        expected = True
        assert (result == expected)

    @staticmethod
    def test_check_header_not_valid():
        result = StateCodeAnalyser.check_header()
        expected = False
        assert (result != expected)

    @staticmethod
    def test_check_delimiter():
        result = StateCodeAnalyser.check_delimiter()
        expected = ','
        assert (result == expected)

    @staticmethod
    def test_check_delimiter_not_valid():
        result = StateCodeAnalyser.check_delimiter()
        expected = '.'
        assert (result != expected)

if __name__ == '__main__':
    Test()
