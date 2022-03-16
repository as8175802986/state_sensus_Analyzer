import pytest
import csv
class StateCensusAnalyser:
    @staticmethod
    def state_census():
        """
            Description:
                Function to load StateCensusData file
            Parameter:
                None
            Return:
                None
        """
        with open("StateCensusData.csv", "r") as data:
            statecensus = csv.DictReader(data, delimiter=',')
            for i in statecensus:
                print(i)

    @staticmethod
    def count_number_records():
        """
            Description:
                Function to count number of records
            Parameter:
                None
            Return:
                rows of records
        """
        #
        with open("StateCensusData.csv") as data:
            statecensus = csv.DictReader(data, delimiter=',')
            for i in statecensus:
                return len(list(statecensus))

if __name__ == '__main__':
    object = StateCensusAnalyser()
    object.count_number_records()