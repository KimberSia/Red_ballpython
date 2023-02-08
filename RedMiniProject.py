#Create Empty List 
List = []

#Populate List Using Apppend 
List.append("Ec2")
List.append("DynamoDb")
List.append("s3")
List.append("Lambda")
List.append("Cloud9")

#Print list and length of the list
print(List)
print(len(List))

#Remove 2 Specific Services From The List By Name
List.remove("Ec2")
List.remove("Lambda")


#Print new list and new length of list
print(List)
print(len(List))

