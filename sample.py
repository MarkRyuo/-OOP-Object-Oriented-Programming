
# * Morning Routine 


class Routine :
    def __init__(self) :
        pass 
        
    def _Routine(self) :
        self.open_social_media()
        self.open_games()

    
    # * Abstract Class

    def open_social_media(self) :
        pass

    def open_games(self) :
        pass


    # * Concrete Class 
class JhonmarkMorningRoutine(Routine) :
    def open_social_media(self) :
        print("Jhon Mark opens Facebook")
    
    def open_games(self) :
        print("Jhon Mark opens Mobile Legends")


class JeromeMorningRoutine(Routine) :
    def open_social_media(self) :
        print("Jerome opens Instagram")
    
    def open_games(self) :
        print("Jerome opens Genshin Impact")


jhonmark_routine = JhonmarkMorningRoutine()
jerome_routine = JeromeMorningRoutine()

jhonmark_routine._Routine()
jerome_routine._Routine()

