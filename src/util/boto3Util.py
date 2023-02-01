import boto3

def S3LsAll(bucket):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket)
    return response


def S3Ls(bucket,path):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket, Prefix=path, Delimiter='/')
    return response

# resource版
def S3LsResource(s3bucket,path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3bucket)
    response = bucket.meta.client.list_objects(Bucket=bucket.name, Prefix=path, Delimiter='/')
    return response

def S3LsResourceContents(s3bucket,path):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3bucket)
    response = bucket.meta.client.list_objects(Bucket=bucket.name, Prefix=path, Delimiter='/')
    return response['Contents']

def S3Download(bucket,targetFile,saveFileName):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    bucket.download_file(targetFile, saveFileName)

def S3Upload(bucket,targetFile,saveFileName):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket)
    bucket.upload_file(saveFileName, targetFile)