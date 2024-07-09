
# * Morning Routine 


class routine :

    def __init__(self) :
        pass 

    def _Routine() :
        self.open_social_media()
        self.open_games()

    
    # * Abstract Class

    def open_social_media(self) :
        pass

    def open_games(self) :
        pass


    # * Concrete Class 
class Jhonmark_morningroutine(routine) :

    def open_social_media(self) :
        print("Jhon Mark opens Facebook")
    
    def open_games(self) :
        print("Jhon Mark opens Mobile Legends")


class Jerome_morningroutine(routine) :

    def open_social_media(self) :
        print("Jerome opens Instagram")
    
    def open_games(self) :
        print("Jerome opens Genshin Impact")


Jhonmark_routine = routine() ;
Jerome_routine = routine()



