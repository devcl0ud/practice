"""String concatination"""

# print('hello' + 'there')

"""practicle example using split and delimitter"""

# exp="Java,python,dot net,c"
# skills=exp.split(',')
# print(skills)
# count=0
# for skill in skills:
#     count=count+1
#     print("my",str(count),"experience is",skill)

"""options to raed number of words"""
"first option,here count letters and spaces"
# text=" my experience with python "
# num_text=text.count('')+1
# print(num_text)

"""second option, here count words"""
# text="my experience with python"
# delimiter =' '
# new_text= text.split(delimiter)
# print(len(new_text))

"""Another example"""
# text="RITU"
# for i in text:
#     print(i)

"Example"
name="my name is ritu"
print(type(name))
new_name=name.split(' ')
print(type(new_name))
