import random

minLen = 100;
maxLen = 200;

class Quote:
    def generateQuote(self):
        sentences = []
        with open("UlyssesText.txt") as f:
            # sentences += re.findall(r".*?[\.\!\?]+", f.read())
            sentences = f.read().split(".")

        sentence = (random.choice(sentences) + ".")

        while (len(sentence)<120 or len(sentence)>400):
            sentence = (random.choice(sentences) + ".")

    # print (sentence)

        return sentence