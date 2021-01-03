import string

"""
Problem:

Need to create a decypher function to unscramble the messages. Test Cases were provided.

The cypher is build such that a would match to z and vice versa. 
"""


def solution(x):
    # Your code here
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    translation = str.maketrans(alphabet, alphabet[::-1])
    result = x.translate(translation)
    
    return result


def main():
   solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
   solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")


if __name__ == "__main__":
    main()

