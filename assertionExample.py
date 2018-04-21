''
'less than 10
spam = int(input("Number>\n"))

assert spam >= 10, "WHOA DUDE!\nWhat the hell do you think you're doing?\nComing into my house, entering values less than 10!"

''
'eggs and bacon
eggs = input("What is eggs?\n")
bacon = input("What da bacons?\n")

assert eggs.lower() != bacon.lower(), "eggs no can the bacon, brah!"

''
'always assert
assert 0>1, "I'M JUST ALWAYS MAD FOR NO REASON!"
