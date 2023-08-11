class Forecast:
    RATINGS = ['low', 'moderate', 'considerable', 'high', 'extreme', 'norating']

    def __init__(self, highlight, alpine, treeline, below_treeline, confidence):
        self.highlight = highlight
        self.alpine = alpine
        self.treeline = treeline
        self.below_treeline = below_treeline
        self.confidence = confidence

    def display(self):
        print(self.highlight)
        print("Alpine: {alpine}".format(alpine=self.alpine))
        print("Treeline: {treeline}".format(treeline=self.treeline))
        print("Below Treeline: {below_treeline}".format(below_treeline=self.below_treeline))