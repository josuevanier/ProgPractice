
import  re
big_sentence = "my cat always finds a way to sneak inside! Every bird loves flying under the bright sky. he enjoys cycling with his dog every morning."




def solution(texts):
    sentences = re.split(r'[(.!?]', texts)
    print(sentences)
    output = []
    for sentence in sentences:
        letters_of_currentSentence = [char for char in sentence if char.isalpha()]
        if letters_of_currentSentence:
            lowest = min(letters_of_currentSentence)
            output.append(lowest)

    return output

print(solution(big_sentence))