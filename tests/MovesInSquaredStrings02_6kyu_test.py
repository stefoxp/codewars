from unittest import TestCase
from MovesInSquaredStrings02_6kyu import rot, selfie_and_rot, oper


class TestRot(TestCase):
    def test_Basic(self):
        self.assertEquals(rot("fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL"),
                          "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif")
        self.assertEquals(rot("rkKv\ncofM\nzXkh\nflCB"),
                          "BClf\nhkXz\nMfoc\nvKkr")


class TestSelfieAndRot(TestCase):
    def test_Basic(self):
        self.assertEquals(selfie_and_rot("xZBV\njsbS\nJcpN\nfVnP"),
                          "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx")
        self.assertEquals(selfie_and_rot("uLcq\nJkuL\nYirX\nnwMB"),
                          "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu")


# class TestOperMirror(TestCase):
#     def test_BasicOper(self):
#         self.assertEquals(oper(selfie_and_rot, "xZBV\njsbS\nJcpN\nfVnP"),
#                           "xZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx")
#         self.assertEquals(oper(selfie_and_rot, "uLcq\nJkuL\nYirX\nnwMB"),
#                           "uLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu")
