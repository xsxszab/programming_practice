class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print "%s: %s" % (self.name, self.score)
stu=student('aaa',95)
stu.print_score()        