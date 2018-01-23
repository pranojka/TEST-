class Comment (object):

    def __init__(self,text,date):

        self.text=text
        self.date=date 



    def __repr__(self):
        return "text: {}.date: {}".format(self.text, self.date)

    # def table(self)    


Comments =[Comment("komentar1","2018-01-23") ,
            Comment ("Komentar2", "2018-01-23") ,
            Comment ("Komentar3", "2018-01-23")]