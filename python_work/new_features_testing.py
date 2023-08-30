python = "pythons"
print(python.title())
print("\tpython")
print("Languages:\nPython\nC\nJavascript")
print("kishan,\nHow are you?\nHope you are good!")
print("Hello\n\tKishan, your cracked at\tFortnite!\nHope you win\tThe next game\nHave fun:)")
favorite_language = ' python p'
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language)
favorite_language = f"{favorite_language.lstrip()}"
nostarch_url = 'https://nostarch.com'
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))
print(nostarch_url)
nostarch_url = f"{nostarch_url.removeprefix('https://')}"
print(nostarch_url)
message = input("Hello, Type anything and I will reply the exact thing you say!")
print(message)
# That is how you do "input" and "output"
# You can also use a dictinary to store one kind of info for many objects!
# For example,
favorite_language = {
    'jen':'python',
    'sarah':'C',
    'edward':'rust',
    'phil':'python',
}
# To use this dictionary, given the name of a person who took the poll, you can easily look up their favorite language:

favorite_language = {
    'jen':'python',
    'sarah':'C',
    'edward':'rust',
    'phil':'python',
}
language = favorite_language['sarah'].title()
print(language)
""" That is how you can use a dictinary. """
# You can apply these situations for other key-values in dictinary's!