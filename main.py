from difflib import get_close_matches
from difflib import SequenceMatcher
from googletrans import Translator
from spanish import words_es
from english import words_en
from hindi import words_hi


def google_check(w):
    detected_lang = (translator.detect(w)).lang
    if detected_lang == "en":
        result.append(w + "_eng")
    elif detected_lang == "es":
        result.append(w + "_spa")
    elif detected_lang == "hi":
        result.append(w + "_hin")

    # if we are still unable to find the language we'll add "_unrec" which means that the language is currently
    # unrecognized by the program .
    else:
        result.append(w + "_unrec")


translator = Translator()
result = []

try:
    # Step1 : Taking a sentence as input and then converting it to a list of words .
    sentence = list(input().split())

    for word in sentence:

        # Step2 : For each word in sentence variable cleaning user utterance .
        word = word.replace("'s", "")
        word = word.replace("_", "")
        word = word.replace(",", "")
        word = word.replace("!", "")
        word = word.replace("?", "")
        word = word.replace(".", "")

        if word:
            # Step3 : Now we will manually search the closest match of the word in the dataset I've downloaded using
            # difflib python library to compare the ratio .
            ratio_en = 0
            ratio_es = 0
            ratio_hi = 0

            en_matches = get_close_matches(word, words_en)
            es_matches = get_close_matches(word, words_es)
            hi_matches = get_close_matches(word, words_hi)

            if len(en_matches) > 0:
                ratio_en = SequenceMatcher(None, en_matches[0], word).ratio()
            if len(es_matches) > 0:
                ratio_es = SequenceMatcher(None, es_matches[0], word).ratio()
            if len(hi_matches) > 0:
                ratio_hi = SequenceMatcher(None, hi_matches[0], word).ratio()

            # We will add the desired annotated text to our result any of the ratio satisfies the condition .
            if ratio_hi > ratio_en and ratio_hi > ratio_es:
                result.append(word + "_hin")

            elif ratio_es > ratio_hi and ratio_es > ratio_en:
                result.append(word + "_spa")

            elif ratio_en > ratio_hi and ratio_en > ratio_es:
                result.append(word + "_eng")
            # At the end if we are unable to find any matches, we'll use google's "googletrans" lib to find the
            # language.
            else:
                google_check(word)

    print(*result)
except:
    print("ERROR!")
