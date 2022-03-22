from state_sensus_Analyzer.state_census_analyzer.indian_state_census_analyzer import StateCensusAnalyser


class Test:
    @staticmethod
    def test_number_records_matches():
        result = StateCensusAnalyser.count_number_records()
        expected = 13
        assert (result == expected)

    @staticmethod
    def test_number_records_not_matches():
        result = StateCensusAnalyser.count_number_records()
        expected = 12
        assert (result != expected)

    @staticmethod
    def test_check_file():
        result = StateCensusAnalyser.check_file()
        expected = "StateCensusData.csv"
        assert (result == expected)

    @staticmethod
    def test_check_file_not_valid():
        result = StateCensusAnalyser.check_file()
        expected = "StausData.csv"
        assert (result != expected)

    @staticmethod
    def test_check_file_extension():
        result = StateCensusAnalyser.check_file_extension()
        expected = ".csv"
        assert (result == expected)

    @staticmethod
    def test_check_file_extension_not_valid():
        result = StateCensusAnalyser.check_file_extension()
        expected = ".pdf"
        assert (result != expected)

    @staticmethod
    def test_check_header():
        result = StateCensusAnalyser.check_header()
        expected = True
        assert (result == expected)

    @staticmethod
    def test_check_header_not_valid():
        result = StateCensusAnalyser.check_header()
        expected = False
        assert (result != expected)

    @staticmethod
    def test_check_delimiter():
        result = StateCensusAnalyser.check_delimiter()
        expected = ','
        assert (result == expected)

    @staticmethod
    def test_check_delimiter_not_valid():
        result = StateCensusAnalyser.check_delimiter()
        expected = '.'
        assert (result != expected)


if __name__ == '__main__':
    Test()
    Test.test_check_file()
