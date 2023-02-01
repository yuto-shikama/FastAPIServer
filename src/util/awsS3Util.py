import subprocess

def S3Ls(path):
    result = subprocess.run(['aws', 's3', 'ls', 's3://'+path], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout.decode()

def S3Upload(targert,path):
    result = subprocess.run(['aws', 's3', 'cp', targert, 's3://'+path], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout.decode()

def S3Download(path,downloadPath):
    result = subprocess.run(['aws', 's3', 'cp', 's3://'+path, downloadPath], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout.decode()

def S3DeleteFile(targert):
    result = subprocess.run(['aws', 's3', 'rm', 's3://'+targert], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout.decode()

def S3DeleteDirectory(targert):
    result = subprocess.run(['aws', 's3', 'rm', 's3://'+targert, '--recursive'], check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return result.stdout.decode()