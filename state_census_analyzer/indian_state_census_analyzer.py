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

    @staticmethod
    def check_file():
        """
            Description:
                Function to ccheck file is exist or not
            Parameter:
                None
            Return:
                None
        """
        try:
            f = open("StateCensusData.csv")
            f.close()
            print("File Exists")
            return "StateCensusData.csv"

        except Exception:
            print("Sorry file does not exist")
        finally :
            print("file check completed")


if __name__ == '__main__':
    StateCensusAnalyser = StateCensusAnalyser()
    StateCensusAnalyser.count_number_records()
    StateCensusAnalyser.check_file()