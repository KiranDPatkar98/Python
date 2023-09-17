# file = open('kdp.text')
# print(file.read())
# print(file.seek(5))

# downloaded this one using pip install translate
from translate import Translator
translator = Translator(to_lang="zh")

try:

    with open('kdp2.txt', 'w') as file:
        translation = translator.translate("How are you ?")
        print(translation)
        print(file.write(translation))
except:
    print('Error occured')
