#Create Empty List 
AWS_List = []

#Populate List Using Append
AWS_List.append("Ec2")
AWS_List.append("DynamoDb")
AWS_List.append("s3")
AWS_List.append("Lambda")
AWS_List.append("Cloud9")

#Print list and length of the list
print(AWS_List)
print(len(AWS_List))

#Remove 2 Specific Services From The List By Name
AWS_List.del("Ec2")
AWS_List.del("Lambda")

#Print new list and new length of list
print(AWS_List)
print(len(AWS_List))

