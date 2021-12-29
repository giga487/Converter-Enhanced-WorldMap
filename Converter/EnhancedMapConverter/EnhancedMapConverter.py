
import os
import os.path
import ntpath

class StringRead:

    def __init__(self, _stringToSplit: str):

        self.m_stringToSplit = _stringToSplit


    def EncapsuleData(self):
        self.m_splittedString = self.m_stringToSplit.split()

        self.m_Name = self.m_splittedString[1] + self.m_splittedString[2]
        self.m_X = self.m_splittedString[3]
        self.m_Y = self.m_splittedString[4]
        self.m_mapIndex = self.m_splittedString[5]
        self.NameInMap = self.m_splittedString[6]
           


class FileToRead:

    def __init__(self, path: str):
        self.m_pathfile = path

    def FindNameGroup(self):
        head, tail = ntpath.split(self.m_pathfile)
        return tail or ntpath.basename(head)


applicationPath = os.getcwd()
folderToAnalyze = "Definition"




def main():

    fileList = os.listdir(os.path.join(applicationPath,folderToAnalyze))

    for fileToAnal in fileList:

        FileToRead(fileToAnal)




if __name__ == "__main__":
    main()