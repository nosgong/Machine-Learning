import webbrowser
class movie():
    def __init__(self, list):
        for key,val in list.items():
            setattr(self,key,val)
    def show_trailer(self):
        webbrowser.open(self.trailer_url)
