import pytest
import csv


class StateCodeAnalyser:

    @staticmethod
    def state_code():
        """
            Description:
                Function to load StateCensusData file
            Parameter:
                None
            Return:
                None
        """
        with open("state_code.csv", "r") as data:
            statecode = csv.DictReader(data, delimiter=',')
            for i in statecode:
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
        with open("state_code.csv") as data:
            statecode = csv.DictReader(data, delimiter=',')
            for i in statecode:
                return len(list(statecode))

    @staticmethod
    def check_file():
        """
            Description:
                Function to check file is exist or not
            Parameter:
                None
            Return:
                None
        """
        try:
            f = open("state_code.csv")
            f.close()
            # print("File Exists")
            return "state_code.csv"
        except Exception:
            print("Sorry file does not exist")

    @staticmethod
    def check_file_extension():
        """
            Description:
                Function to check csv file exists or not
            Parameter:
                None
            Return:
                .csv
        """
        try:
            file = "state_code.csv"
            result = file.endswith(".csv")
            if result:
                return ".csv"
            else:
                raise Exception(StateCodeAnalyser)
        except StateCodeAnalyser:
            print("Sorry! CSV file does not exist")

    @staticmethod
    def check_header():
        """
            Description:
                Function to check header is present or not
            Parameter:
                None
            Return:
                .csv
        """
        try:
            with open("state_code.csv", "r") as data:
                headers = csv.Sniffer().has_header(data.read())
                if headers:
                    return headers
                else:
                    raise Exception(StateCodeAnalyser)
        except StateCodeAnalyser:
            print("headers Not found")

    @staticmethod
    def check_delimiter():
        """
            Description:
                Function to check delimiter is correct or not
            Parameter:
                None
            Return:
                delimiter
        """
        try:
            with open("state_code.csv", 'r', newline='') as data:
                dialect = csv.Sniffer().sniff(data.read())
                if dialect.delimiter == ',':
                    return dialect.delimiter
                else:
                    raise Exception(StateCodeAnalyser)
        except StateCodeAnalyser:
            print("Incorrect delimiter found")


if __name__ == '__main__':
    StateCodeAnalyser=StateCodeAnalyser()
    StateCodeAnalyser.state_code()
    StateCodeAnalyser.count_number_records()
    StateCodeAnalyser.check_file()
    StateCodeAnalyser.check_header()
    StateCodeAnalyser.check_file_extension()
    StateCodeAnalyser.check_delimiter()
