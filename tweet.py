import  point

#Tweet class  be created that contains (composition) a Point object.
class Tweet():

    def __init__(self,point,text,source,id_str,lang,created_time):

        self.point=point    #The tweet spatial information
        self.text=text      #The text
        self.source=source  #the source
        self.id_str=id_str  #the id_str
        self.lang=lang      #the language
        self.created_time=created_time   #the create time

    def get_spatial_information(self):
        """
         Return the tweet spatial information.
        :return:(lat,lon)
        """
        return (self.point.x,self.point.y)