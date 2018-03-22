class movie():
    def __init__(self, list):
        for key,val in list.items():
            setattr(self,key,val)
    def outputName(self):
        print self.title
