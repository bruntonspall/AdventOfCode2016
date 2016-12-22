import unittest
import bot


class BotTest(unittest.TestCase):
    def test_connect_bots(self):
        o0 = bot.Output()
        o1 = bot.Output()
        o2 = bot.Output()
        b0 = bot.Bot("b0", o0, o2)
        b1 = bot.Bot("b1", b0, o1)
        b2 = bot.Bot("b2", b0, b1)
        b2.giveValue(5)
        b1.giveValue(3)
        b2.giveValue(2)

        self.assertEquals([5, 2], b2.compared)

    def test_parse(self):
        inp = [
                "value 5 goes to bot 2",
                "bot 2 gives low to bot 1 and high to bot 0",
                "value 3 goes to bot 1",
                "bot 1 gives low to output 1 and high to bot 0",
                "bot 0 gives low to output 2 and high to output 0",
                "value 2 goes to bot 2"]

        bots, outputs = bot.parse(inp)
        self.assertEquals(3, len(bots))
        self.assertEquals(3, len(outputs))
        self.assertEquals(bots[0], bots[2].hi)
        self.assertEquals(bots[1], bots[2].lo)
        self.assertEquals(outputs[1], bots[1].lo)
        self.assertEquals(bots[0], bots[1].hi)
        self.assertEquals(outputs[0], bots[0].hi)
        self.assertEquals(outputs[2], bots[0].lo)
        self.assertEquals([5, 3], bots[0].compared)
        self.assertEquals([3, 2], bots[1].compared)
        self.assertEquals([2, 5], bots[2].compared)
