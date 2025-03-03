import os

import groupdocs_comparison_cloud


class Common_Utilities:

    # Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
    app_sid = None
    app_key = None
    host_url = None
    myStorage = None
    
    @classmethod
    def Get_CompareApi_Instance(self):
        # Create instance of the API
        return groupdocs_comparison_cloud.CompareApi.from_keys(Common_Utilities.app_sid, Common_Utilities.app_key)
    
    @classmethod
    def Get_InfoApi_Instance(self):
        # Create instance of the API
        return groupdocs_comparison_cloud.InfoApi.from_keys(Common_Utilities.app_sid, Common_Utilities.app_key)
    
    @classmethod
    def Get_SignApi_Instance(self):
        # Create instance of the API
        return groupdocs_comparison_cloud.SignApi.from_keys(Common_Utilities.app_sid, Common_Utilities.app_key)
    
    @classmethod
    def Get_StorageApi_Instance(self):
        # Create instance of the API
        return groupdocs_comparison_cloud.StorageApi.from_keys(Common_Utilities.app_sid, Common_Utilities.app_key)
    
    @classmethod
    def Get_FolderApi_Instance(self):
        # Create instance of the API
        return groupdocs_comparison_cloud.FolderApi.from_keys(Common_Utilities.app_sid, Common_Utilities.app_key)
    
    @classmethod
    def Get_FileApi_Instance(self):
        # Create instance of the API
        return groupdocs_comparison_cloud.FileApi.from_keys(Common_Utilities.app_sid, Common_Utilities.app_key)
      
    @classmethod  
    def Upload_Test_Files(self):
        
        dirName = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\Resources\\comparisondocs\\"
        print("dirName: " + dirName)
        TestFiles = Common_Utilities.getListOfFiles(dirName)
        
        # api initialization
        storageApi = Common_Utilities.Get_StorageApi_Instance()
        fileApi = Common_Utilities.Get_FileApi_Instance()
        
        print("Files Count: " + str(len(TestFiles)))
        
        for item in TestFiles:
            print("File to Upload: "+ dirName + item)
            # skip existing file uploading
            fileExistRequest = groupdocs_comparison_cloud.ObjectExistsRequest(dirName + item)
            fileExistsResponse = storageApi.object_exists(fileExistRequest)
            if not fileExistsResponse.exists:                
                # file content uploading
                putCreateRequest = groupdocs_comparison_cloud.UploadFileRequest('comparisondocs\\' + item, dirName + item)
                fileApi.upload_file(putCreateRequest)
                print("Uploaded missing file: "+ 'comparisondocs\\' + item)
        
        print("File Uploading completed..")
        
    @classmethod  
    def getListOfFiles(self, dirName):
        # create a list of file and sub directories 
        # names in the given directory 
        listOfFile = os.listdir(dirName)
        allFiles = list()
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join("", entry)
            # If entry is a directory then get the list of files in this directory 
            if os.path.isdir(fullPath):
                allFiles = allFiles + Common_Utilities.getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)
                    
        return allFiles