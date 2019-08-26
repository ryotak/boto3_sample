import boto3

# access_key = AWSのアクセスキー
# secret_key = AWSのシークレットキー
# region = AWSのリージョンを泡らす文字列　例）'ap-northeast-1'　東京リージョン
#
# ec2 = boto3.resource('ec2',
#                      aws_access_key_id=access_key,
#                      aws_secret_access_key=secret_key,
#                      region_name=region
#                      )
#
# 下記の環境変数を使うことにより省略して書くことができる
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY
# AWS_DEFAULT_REGION
#

ec2 = boto3.resource('ec2')

# インスタンス作成
AMI_ID = 'ami-0c3fd0f5d33134a76'
SUBNET_ID = 'subnet-xxx'  # サブネットIDを指定

instances = ec2.create_instances(ImageId=AMI_ID,
                                 MaxCount=1, MinCount=1,
                                 InstanceType='t2.micro',
                                 SubnetId=SUBNET_ID)
print(instances)
instance = instances[0]

# 起動まで待つ
instance.wait_until_running()

# instance type 取得
it = instance.describe_attribute(Attribute='instanceType')
print(it)
print("InstanceType = {}".format(it.get('InstanceType')))

# IPアドレスなど取得
ni = instance.network_interfaces_attribute
print(ni)

# インスタンスを終了させる
tm = instance.terminate()
print(tm)

# 終了まで待つ
instance.wait_until_terminated()
