from fastapi import APIRouter
import util.boto3Util as boto
import json
from pydantic import BaseModel, EmailStr
from typing import List
from fastapi.responses import FileResponse
import datetime

router = APIRouter(
    prefix='/api/s3',
    tags=['awsS3']
)

class FileData(BaseModel):
    name: str
    date: str
    size: int

class FileDatas(BaseModel):
    datas:List[FileData]

# S3の指定のパスの中身を取得する
@router.get("/ls",response_model=FileDatas)
async def s3_ls(buket,path = ''):
    objs = boto.S3LsResourceContents(buket,path)

    resultDatas = list()
    for obj in objs['Contents']:
        dateStr = obj['LastModified'].strftime("%Y/%m/%d %H:%M:%S")
        data = FileData(name = obj['Key'],date = dateStr,size = obj['Size'])
        resultDatas.append(data)

    fileDatas = FileDatas(datas = resultDatas)
    return fileDatas

# S3の指定のパスにファイルをアップロード
@router.put("/upload")
async def s3_upload(buket,saveFileName,targetFile):
    return boto.S3Upload(buket,targetFile, "./tmp/upload/" + saveFileName)

# S3の指定のパスにファイルをダウンロード
@router.get("/download")
async def s3_download(buket,saveFileName,targetFile):
    downloadPath = "./tmp/download/" + saveFileName
    boto.S3Download(buket,targetFile,downloadPath)
    header = {'Content-Disposition': 'attachment; filename=' + saveFileName}
    return FileResponse(downloadPath,headers=header)

# S3の指定のパスにファイルを削除
@router.put("/delete")
async def s3_delete(targetFile,path):
    return "未実装"