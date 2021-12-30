
import os
import os.path
import ntpath

class StringRead:
    DEFAULT_ZOOM_LEVEL = 0
    DEFAULT_COLOR = "white"
    
    FILE_TO_IMAGE = {
        "BANK.txt":"BANK", "LOGS.txt":"LOGS","HIDES.txt":"HIDES","COTTON.txt":"COTTON","INGRESSO.txt":"INGRESSO","NORMALWOOD.txt":"NORMALWOOD","SPIDERROCKS.txt":"SPIDERROCKS","BRDIGE.txt":"BRDIGE",
        "MINER.txt":"MINER","FISH.txt":"FISH", "NORMALHIDES.txt":"NORMALHIDES","STRONGSHRUB.txt":"STRONGSHRUB","EXTWORKERPOINT.txt":"EXTWORKERPOINT", "DUNGEONSPOT.txt":"DUNGEONSPOT",
        "SAND.txt":"SAND","VULCANO.txt":"VULCANO","CAVEAU.txt":"CAVEAU","SHELLS.txt":"SHELLS","MARKET.txt":"MARKET","PRISON.txt":"PRISON","PORT.txt":"PORT","INN.txt":"INN", "INTEREST.txt":"INTEREST",
        "TOWN.txt":"TOWN", "OUTPOST.txt":"OUTPOST","MOONGATE.txt":"MOONGATE", "CASTLE.txt":"CASTLE", "EXIT.txt":"EXIT","WORKERPOINT.txt":"WORKERPOINT", 
    }

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

            fileName = self.FindNameGroup()

            if(fileName in self.FILE_TO_IMAGE):

                self.m_stringToSave = f"{self.m_X},{self.m_Y},{self.m_mapIndex},{self.m_Name}0,{self.FILE_TO_IMAGE[fileName]},{self.DEFAULT_COLOR},{self.DEFAULT_ZOOM_LEVEL}"

            else:
                self.m_stringToSave = f"{self.m_X},{self.m_Y},{self.m_mapIndex},{self.m_Name},{self.DEFAULT_COLOR},{self.DEFAULT_ZOOM_LEVEL}"
            print(self.m_stringToSave)

        except:
            print(f"Error on parse string \"{self.m_stringToSplit}\" in file {self.m_pathfile}")
           
class FileWriter:

    @staticmethod
    def __init__(_pathFiles: str, listOfRow):
      
        f = open(_pathFiles, 'w+')

        for row in listOfRow:
            f.writelines(row+'\n')



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

        if(self.m_listLine != []):
            for line in self.m_listLine:
                m_list.append(line.GetString())
    
        return m_list

applicationPath = os.getcwd()
projectPath = os.path.abspath(os.path.join(applicationPath,'..\..'))
folderToAnalyze = "Definitions"
fileToCreate = "UOMARS.csv"


def main():
    print("Welcome to the enhanced map Converter by Giga487")
    pathToAnalyze = os.path.join(projectPath, folderToAnalyze)
    print(f"Analyze the path {pathToAnalyze}")

    if(not os.path.exists(pathToAnalyze)):
        print(f"Cannot analyze the path {pathToAnalyze}")
    else:
        
        fileList = os.listdir(pathToAnalyze)

        listFile = []
        textOnFileToWrite = []

        for fileToAnal in fileList:

            listFile.append(FileToRead(os.path.join(pathToAnalyze, fileToAnal)))

        for listFileToWrite in listFile:
            if(listFileToWrite.GetString() != []):

                for row in listFileToWrite.GetString():
                    textOnFileToWrite.append(row)

        FileWriter(os.path.join(projectPath, fileToCreate), textOnFileToWrite)

    text = input("")


if __name__ == "__main__":
    main()