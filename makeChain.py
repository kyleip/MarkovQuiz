import markovify


class Chain:
    def genereteChain(self):

        with open("UlyssesText.txt") as f:
            text = f.read()

            text_model = markovify.Text(text)

        # print(text_model.make_short_sentence(250,120))

        return (text_model.make_short_sentence(200,100))