
import os
import os.path
import ntpath
from typing import ItemsView
import logging

class StringRead:
    DEFAULT_ZOOM_LEVEL = 0
    DEFAULT_COLOR = "white"

    def __init__(self, _stringToSplit: str, _file):

        self.m_stringToSplit = _stringToSplit
        self.m_pathfile = _file
        self.m_stringToSave = ""
        self.EncapsuleData()

    def GetString(self):
        return self.m_stringToSave

    def FindNameGroup(self):
        head, tail = ntpath.split(self.m_pathfile)
        return tail or ntpath.basename(head)

    def EncapsuleData(self):

        self.m_splittedString = self.m_stringToSplit.split(';')
        self.m_Name = ""

        IsNotCoordinate = True
        #starto da dopo il +
        i = 1

        try:

            while IsNotCoordinate == True:

                try:
                    intValueToCheck = int(self.m_splittedString[i])
                    IsNotCoordinate = False
                    break
                except:
                    self.m_Name += " " + self.m_splittedString[i]
                i += 1

            self.m_X = self.m_splittedString[i]
            i+=1
            self.m_Y = self.m_splittedString[i]
            i+=1
            self.m_mapIndex = self.m_splittedString[i]
            i+=1
            self.NameInMap = self.m_splittedString[i]     

            fileName = self.FindNameGroup()
            fileToSearch = fileName.replace(".txt","")

            self.m_stringToSave = f"{self.m_X},{self.m_Y},{self.m_mapIndex},{self.m_Name},{fileToSearch},{self.DEFAULT_COLOR},{self.DEFAULT_ZOOM_LEVEL}"

            print(self.m_stringToSave)

        except:
            print(f"Error on parse string \"{self.m_stringToSplit}\" in file {self.m_pathfile}")
           
class FileWriter:

    @staticmethod
    def __init__(_pathFiles: str, listOfRow):
        try:

            f = open(_pathFiles, 'w+')

            for row in listOfRow:
                f.writelines(row+'\n')

            print("\n")
            print(f"File created at {_pathFiles}")
        except:
            print("Error on output creation file")


class LineInfo:

    def __init__(self, line: str, IsLineToSave: bool):
        self.m_newString = line
        self.m_toSave = IsLineToSave

    def GetString(self):
        return self.m_newString

    def IsToSave(self):
        return self.m_toSave

class LineConverter:

     @staticmethod
     def OldToNewFOrmat(_strToAnalyze) -> LineInfo:

        if(_strToAnalyze.find(";") != -1):  #is already converted
            stringToReturn = LineInfo(_strToAnalyze, False)
        else:
            stringSplitted = _strToAnalyze.split()
            Name = ""
            IsNotCoordinate = True
            SymbolAdd = stringSplitted[0]

            i = 1
            try:
                while IsNotCoordinate == True:

                    try:
                        intValueToCheck = int(stringSplitted[i])
                        IsNotCoordinate = False
                        break
                    except:
                        Name += " " + stringSplitted[i]
                    i += 1
                     
                X = intValueToCheck
                i+=1
                Y = stringSplitted[i]
                i+=1
                Map = stringSplitted[i]
                i+=1
                IsVisible = stringSplitted[i]

                stringToReturn = LineInfo(f"{SymbolAdd};{Name};{X};{Y};{Map};{IsVisible}\n", True)
            except:
                print(f"Error on convert string to new format")
                stringToReturn = LineInfo(_strToAnalyze, False)

        return stringToReturn


class FileToRead:

    def __init__(self, path: str):
        self.m_pathfile = path

        self.LoadFiles()


    def FindNameGroup(self):
        head, tail = ntpath.split(self.m_pathfile)
        return tail or ntpath.basename(head)

    def LoadFiles(self):

        self.m_listLine = []
        self.newLines = []
        try:
            with open(self.m_pathfile, 'r') as f:
                lines = f.readlines()

            if(lines != []):

                for line in lines:
                
                    stringToStudy = LineConverter.OldToNewFOrmat(line)
                    self.newLines.append(stringToStudy.GetString())
            
                with open(self.m_pathfile, 'w') as f:
                    for line in self.newLines:
                        f.write(line)

                print(f"\nRead file {self.FindNameGroup()} ++++++++++++")

                for line in self.newLines:

                    stringToStudy = LineConverter.OldToNewFOrmat(line)                    
                    self.m_listLine.append(StringRead(stringToStudy.GetString(), self.m_pathfile))

        except:
            print("Error")

    def GetString(self):

        m_list = []

        if(self.m_listLine != []):
            for line in self.m_listLine:
                m_list.append(line.GetString())
    
        return m_list

applicationPath = os.getcwd()
folderToAnalyze = "Definitions"
fileToCreate = "UOMARS.csv"


def main():
    logging.basicConfig(filename="appLog.log", filemode='w+', level=logging.WARN)
    print("Welcome to the enhanced map Converter by Giga487")
    pathToAnalyze = os.path.join(applicationPath, folderToAnalyze)


    if(not os.path.exists(pathToAnalyze)):
        print(f"Cannot analyze the path {pathToAnalyze}")
    else:
        print(f"Analyze the path {pathToAnalyze}")
        fileList = os.listdir(pathToAnalyze)

        listFile = []
        textOnFileToWrite = []

        for fileToAnal in fileList:


            listFile.append(FileToRead(os.path.join(pathToAnalyze, fileToAnal)))

        for listFileToWrite in listFile:
            if(listFileToWrite.GetString() != []):

                for row in listFileToWrite.GetString():
                    textOnFileToWrite.append(row)

        FileWriter(os.path.join(applicationPath, fileToCreate), textOnFileToWrite)

    text = input("")


if __name__ == "__main__":
    main()