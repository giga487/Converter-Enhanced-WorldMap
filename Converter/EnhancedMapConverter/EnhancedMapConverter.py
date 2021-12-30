
import os
import os.path
import ntpath

class StringRead:
    DEFAULT_ZOOM_LEVEL = 0
    DEFAULT_COLOR = "white"

    def __init__(self, _stringToSplit: str, _file):

        self.m_stringToSplit = _stringToSplit
        self.m_pathfile = _file
        self.EncapsuleData()

    def GetString(self):
        return self.m_stringToSave

    def EncapsuleData(self):
        self.m_splittedString = self.m_stringToSplit.split()

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

            self.m_stringToSave = f"{self.m_X},{self.m_Y},{self.m_mapIndex},{self.m_Name},{self.DEFAULT_COLOR},{self.DEFAULT_ZOOM_LEVEL}"
            print(self.m_stringToSave)

        except:
            print(f"Error on parse string \"{self.m_stringToSplit}\" in file {self.m_pathfile}")
           
class FileWriter:

    def __init__(self, _pathFiles: str, ):
        print("BOH")



class FileToRead:

    def __init__(self, path: str):
        self.m_pathfile = path

        self.LoadFiles()


    def FindNameGroup(self):
        head, tail = ntpath.split(self.m_pathfile)
        return tail or ntpath.basename(head)

    def LoadFiles(self):

        self.m_listLine = []

        try:
            with open(self.m_pathfile) as f:
                lines = f.readlines()

            if(lines != []):
                print(f"\n+++++++++++ Read file {self.FindNameGroup()} ++++++++++++")
                for line in lines:
                    self.m_listLine.append(StringRead(line, self.m_pathfile))
        except:
            print("Error")

    def GetString(self):

        m_list = []
        for line in self.m_listLine:
            m_list.append(line.GetString())
    
        return m_list


applicationPath = os.getcwd()
folderToAnalyze = "Definitions"

def main():
    print("Welcome to the enhanced map Converter by Giga487")
    pathToAnalyze = os.path.join(applicationPath, folderToAnalyze)
    print(f"Analyze the path {pathToAnalyze}")
    fileList = os.listdir(pathToAnalyze)

    listFile = []
    textOnFileToWrite = []

    for fileToAnal in fileList:

        listFile.append(FileToRead(os.path.join(pathToAnalyze, fileToAnal)))

    for listFileToWrite in listFile:
        textOnFileToWrite.append(listFileToWrite.GetString())

    text = input("")


if __name__ == "__main__":
    main()