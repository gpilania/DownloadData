import requests

# 读取的文件目录
reader_file = "/Users/yanmeng/Downloads/test.txt"
# 存放的文件夹路径
output_dictionary = "/Users/yanmeng/Downloads/chenzijuan/"


def download(url,index):
    r = requests.get(url)
    with open(output_dictionary+str(index)+str(url.split('?')[0].split('/')[-1]), "wb") as code:
        code.write(r.content)
        code.close()

# f = open(reader_file)
# lines = f.readlines()
# index = 0;
# for line in lines:
#     index = index+1
#     line = line.replace('\n','',1)
#     print(line)
#     download(line, index)
# f.close()

download("http://101.201.177.119/dlcdc/space/gpfs01/sdb/sdb_files/datasets/SURF_CLI_CHN_MUL_DAY_V3.0/datasets/TEM/SURF_CLI_CHN_MUL_DAY-TEM-12001-200506.TXT?Expires=1517978555&OSSAccessKeyId=CcULE6lAfEbIFtKD&Signature=8OpHUv1labPEv5UN2j9i2rIT28A%3D",239)



