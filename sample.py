
# * Morning Routine 


class Routine :

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
class Jhonmarkmorningroutine(Routine) :

    def open_social_media(self) :
        print("Jhon Mark opens Facebook")
    
    def open_games(self) :
        print("Jhon Mark opens Mobile Legends")


class Jeromemorningroutine(Routine) :

    def open_social_media(self) :
        print("Jerome opens Instagram")
    
    def open_games(self) :
        print("Jerome opens Genshin Impact")


jhonmark_routine = Jhonmarkmorningroutine()
jerome_routine = Jeromemorningroutine()


jhonmark_routine._Routine()
jerome_routine._Routine()

