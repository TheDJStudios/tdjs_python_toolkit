import json
import struct


class BEncode:
    def __init__(self, dictionary: str):
        self.dict = json.loads(dictionary)
        self.ids = {}

        for k, v in self.dict.items():
            self.ids[str(v)] = k

    def encode(self, inp: str):
        out = b""
        for item in inp.split():
            if item in self.dict:
                buffer = self.dict[item]
                out += buffer.to_bytes(4, "little")
        return out

    def decode(self, inp:bytes):
        out = ""
        for (value,) in struct.iter_unpack("<I",inp):
            out += f"{self.ids[str(value)]} "
        return out