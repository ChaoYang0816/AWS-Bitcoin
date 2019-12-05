import boto3
import re

userdata = """
#!/bin/bash
wget https://cccoursework816.s3.amazonaws.com/test.py
yum -y install python3
python3 test.py {} {} {} {}
"""

def getClient():
    Client = boto3.client('ec2')
    return Client


def CreateInstance(Client,userdata):
    resp = Client.run_instances(ImageId='ami-00068cd7555f543d5',
                         InstanceType='t2.micro',
                         MinCount=1,
                         MaxCount=1,
                         KeyName='WindowsKP',
                         SecurityGroups=['launch-wizard-2'],
                         SecurityGroupIds=['sg-046b743a51bf611b9'],
                         UserData=userdata,)
    getInstanceId = list(map(lambda x: {"InstanceId": x['InstanceId']}, resp['Instances']))
    return getInstanceId


def CreateMultipleInstance(Client,InsN, Difficult_Level, UserInput):
    InstanceList = []
    for i in range(InsN):
        Instance = CreateInstance(Client, userdata=userdata.format(InsN, Difficult_Level, UserInput, i))
        InstanceList += Instance
    return InstanceList


def main(InsN, Difficult_Level, UserInput):
    Client = getClient()
    InstanceList = CreateMultipleInstance(Client, InsN, Difficult_Level, UserInput)
    InstanceListIds = list(map(lambda x: x['InstanceId'], InstanceList))
    while True:
        for instance in InstanceListIds:
            Output = Client.get_console_output(DryRun=False, InstanceId=instance)
            if Output.get("Output"):
                nonce = re.findall(r"Nonce is:(.*)", Output.get("Output"))
                if nonce:
                    print("Nonce is:", nonce[0])
                    text = re.findall(r"Text is:(.*)", Output.get("Output"))
                    print("Text is:", text[0])
                    RunningTime = re.findall(r"Total Running Time:(.*)", Output.get("Output"))
                    print("Total Running Time:", RunningTime[0])
                    Client.terminate_instances(InstanceIds=InstanceListIds)
                break
            break

if __name__ == '__main__':
    num_vm = input("Input the number of virtual machine that you want to run")
    difficult_level = input("Input the difficulty level that you want to run")
    user_input = input("Type the text you want to analyse")
    main(int(num_vm), int(difficult_level), user_input)
