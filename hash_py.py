
def solution(sentence):
    words = sentence.split(" ")
    my_counter = {}

    for word in words:
        my_counter[word] = my_counter.get(word,0) + 1
     
    print(my_counter.items())
    counted = sorted(my_counter.items(), key=lambda x:-x[my_counter[word]])
    print(counted[0][0])
    return counted[0][0]

if __name__ == '__main__':
    sentence ="demi is very very lazy"
    solution(sentence)