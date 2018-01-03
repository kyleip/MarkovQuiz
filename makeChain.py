import markovify


class Chain:
    def genereteChain(self):

        with open("UlyssesText.txt") as f:
            text = f.read()

            text_model = markovify.Text(text)

        # print(text_model.make_short_sentence(250,120))
        sentence = text_model.make_short_sentence(400,140)
        while(sentence is None):
            sentence = text_model.make_short_sentence(400, 140)

        return (sentence)