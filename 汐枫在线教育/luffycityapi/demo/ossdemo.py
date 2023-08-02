import oss2, uuid

if __name__ == '__main__':
    OSS_ACCESS_KEY_ID = "LTAI5tJMY52AKHxRXayMjNdf"
    OSS_ACCESS_KEY_SECRET = "nKAfpAAgbHFy01BVjJvEKpL8VlElGG"
    OSS_ENDPOINT = "oss-cn-shanghai.aliyuncs.com"  # 访问域名, 根据服务器上的实际配置修改
    OSS_BUCKET_NAME = "luffycityyehuo"  # oss 创建的 BUCKET 名称

    OSS_SERVER_URL = f"https://{OSS_BUCKET_NAME}.{OSS_ENDPOINT}"

    # 创建命名空间操作实例对象
    auth = oss2.Auth(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET)
    bucket = oss2.Bucket(auth, OSS_ENDPOINT, OSS_BUCKET_NAME)

    # 上传文件
    image = f"demo/{str(uuid.uuid4())}.jpg"
    with open('/home/moluo/Desktop/luffycity/luffycityapi/luffycityapi/uploads/avatar/2021/avatar.jpg', "rb") as f:
        result = bucket.put_object(image, f.read())
        print(result)
        print(result.status)
        print(f"{OSS_SERVER_URL}/{image}")
