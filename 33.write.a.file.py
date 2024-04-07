
# text = "Yoooooooooo\nThis is some text\nHave a good one!\n"
# text = "Uh oh! This text has been overwritten"
text = "Have a nice day! See ya"

with open('test.txt','a') as file:
    file.write(text)

