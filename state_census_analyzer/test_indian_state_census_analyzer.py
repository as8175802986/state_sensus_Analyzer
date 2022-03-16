from state_census_analyzer.indian_state_census_analyzer import StateCensusAnalyser

class Test:
    @staticmethod
    def test_number_records_matches():
        assert StateCensusAnalyser.count_number_records() == 13

    @staticmethod
    def test_check_file():
        assert StateCensusAnalyser.check_file() == "StateCensusData.csv"

    @staticmethod
    def test_check_file_extension():
        assert StateCensusAnalyser.check_file_extension() == ".csv"

    @staticmethod
    def test_check_header():
        assert StateCensusAnalyser.check_header() == True

    @staticmethod
    def test_check_delimiter():
        assert StateCensusAnalyser.check_delimiter() == ","

if __name__ == '__main__':
    Test()