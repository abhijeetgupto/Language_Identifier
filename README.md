# Language_Identifier
A python code using difflib and googletrans to distinguish languages. 


• To run the project please run main.py file and input a string of words to convert.


How’s the project working?


In this project I’ve mainly used two python libraries for more accurate results namely:


1. difflib – I’ve downloaded datasets for each language and this using this library the code
checks the probability of the word in each language dataset. So, if that ratio is maximum
in one of the languages that language is considered.


Advantage:
• The accuracy can be really good.
• In future if we can get a better dataset, accuracy can be further improved
• It is easy to implement and mange

Disadvantage:
• Using a wide dataset increases the size of the project
• Since we are searching manually in each of these big datasets, the speed if the
code is quite slow.
So, if after using this method if we are unable to identify the language, I’m using google’s
googletrans lib to identify further.

2. googletrans – This is a python library by google to translate and identify languages.
Advantage:
• This library is really
Disadvantage:
• This library is good when there is only one language in a sentence but if there
are multiple language in a sentence it is not that accurate.
• It is not accurate for detecting language of just one word.
