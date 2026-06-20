import json


class NumEncode:
    def __init__(self, dictionary):

        self.wordid = json.loads(dictionary)

        self.idword = {}

        for k, v in self.wordid.items():
            self.idword[str(v)] = k

    def encode(self, inpu):
        out = ""
        for word in inpu.split():
            if word.lower() in self.wordid:
                out += f"{self.wordid[word.lower()]} "
            else:
                out += f"{word.lower()} "
        return out

    def decode(self, inpu):
        outp = ""
        for pawn in inpu.split():
            if pawn in self.idword:
                outp += f"{self.idword[pawn]} "
            else:
                outp += f"{pawn} "
        return outp