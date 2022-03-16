from state_census_analyzer.indian_state_census_analyzer import StateCensusAnalyser

class Test:
    @staticmethod
    def test_number_records_matches():
        assert StateCensusAnalyser.count_number_records() == 13

    @staticmethod
    def test_check_file():
        assert StateCensusAnalyser.check_file() == "StateCensusData.csv"

if __name__ == '__main__':
    Test()