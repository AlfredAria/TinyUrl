from django.test import TestCase
from url.codec import Codec

# Create your tests here.
class CodecTest(TestCase):
    def setUp(self):
        None

    def test_encode_works(self):
        self.assertEqual(Codec.encode(1), "000001")

    def test_decode_works(self):
        self.assertEqual(Codec.decode("000001"), 1)

    def test_long_to_short_works(self):
        self.assertRegex(Codec.long_to_short("www.google.com"), r".+/000001")

    def test_short_to_long_works(self):
        url = Codec.long_to_short("www.google.com")
        self.assertEqual(Codec.short_to_long(url), "www.google.com")

from url.views import append_protocol_name

class ViewsTest(TestCase):

    def test_append_protocol_name(self):
        self.assertEqual(append_protocol_name("www.google.com"), "http://www.google.com")

    def test_append_protocol_name_with_http(self):
        self.assertEqual(append_protocol_name("http://www.google.com"), "http://www.google.com")

    def test_append_protocol_name_with_http(self):
        self.assertEqual(append_protocol_name("https://www.google.com"), "https://www.google.com")