import boto3

def list_groups():

    client = boto3.client('iam')
    list_iam_groups = client.list_groups()
    # print(list_iam_groups['Groups'])
    for j in list_iam_groups['Groups']:
        print(j['GroupName'], j['GroupId'], j['CreateDate'], j['Path'])

def main():
    print("The IAM groups are.....")
    list_groups()
main()
