from state_census_analyzer.indian_state_census_analyzer import StateCensusAnalyser

class Test:
    @staticmethod
    def test_number_records_matches():
        assert StateCensusAnalyser.count_number_records() == 13

if __name__ == '__main__':
    Test()