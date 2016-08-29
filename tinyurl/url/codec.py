from url.models import LongUrl
import socket

try:
    HOSTNAME = socket.gethostbyname(socket.gethostname())
except:
    HOSTNAME = 'localhost'

BASE62="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

class Codec:
    @staticmethod
    def long_to_short(longurl):
        index = -1
        if LongUrl.objects.filter(url=longurl).count() > 0:
            index = LongUrl.objects.filter(url=longurl).first().id
        else:
            longUrlObj = LongUrl(url=longurl)
            longUrlObj.save()
            index = longUrlObj.id
        print(index)
        return "http://" + HOSTNAME + ":8000/url/" + Codec.encode(index)

    @staticmethod
    def short_to_long(short):
        base62 = short.split("/")[-1]
        index = Codec.decode(base62)
        if LongUrl.objects.filter(id=index).count() > 0:
            return LongUrl.objects.filter(id=index).first().url
        else:
            return ""

    @staticmethod
    def decode(s):
        i = 0
        mul = 1
        for c in s[::-1]:
            i += BASE62.index(c) * mul
            mul *= 62
        return i

    @staticmethod
    def encode(index):
        s = ""
        while index > 0:
            s = BASE62[index % 62]
            index = int(index / 62)
        while len(s) < 6:
            s = "0" + s
        return s