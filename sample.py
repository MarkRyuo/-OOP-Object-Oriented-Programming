
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
class Jhonmarkmorningroutine(routine) :

    def open_social_media(self) :
        print("Jhon Mark opens Facebook")
    
    def open_games(self) :
        print("Jhon Mark opens Mobile Legends")


class Jeromemorningroutine(routine) :

    def open_social_media(self) :
        print("Jerome opens Instagram")
    
    def open_games(self) :
        print("Jerome opens Genshin Impact")


Jhonmark_routine = Jhonmarkmorningroutine()
Jerome_routine = Jeromemorningroutine()


Jhonmark_routine._routine()
Jerome_routine._routine()

