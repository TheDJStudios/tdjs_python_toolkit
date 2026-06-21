import json
import struct


class NumEncode:
    def __init__(self, dictionary: str):

        self.wordid = json.loads(dictionary)

        self.idword = {}

        for k, v in self.wordid.items():
            self.idword[str(v)] = k

    def encode(self, inpu: str):
        out = ""
        for word in inpu.split():
            if word.lower() in self.wordid:
                out += ".-"
                out += f"{self.wordid[word.lower()]} "
            else:
                out += f"{word.lower()} "
        return out

    def decode(self, inpu: str):
        outp = ""
        for pawn in inpu.split():
            if pawn.lstrip(".-") in self.idword:
                outp += f"{self.idword[pawn.lstrip(".-")]} "
            else:
                outp += f"{pawn} "
        return outp