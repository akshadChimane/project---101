from posixpath import relpath
import dropbox
import os 
from dropbox.files import WriteMode

class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken

    def uploadfiles(self,file_from,file_too):
        dbx=dropbox.Dropbox(self.accesstoken)
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                localpath=os.path.join(root,filename)
                rpath=os.path.relpath(localpath,file_from,)
                dpath=os.path.join(file_too,rpath)
                with open(localpath,"rb")as f:
                    dbx.file_upload(f.read(),dpath,mode=WriteMode("overwrite"))

def main():
    access_token="jLm41yuWYbEAAAAAAAAAAWJz_Hp4xiJXaheAwikd8egTtO5dW_-iVSIqYGGIXM-o"    
    transferData=Transferdata(access_token)
    file_from=input("enter the file to tranfer")
    file_to=input("enter the path in dropbox")
    transferData.uploadfiles(file_from,file_to)

    print("file has been moved")

main()    