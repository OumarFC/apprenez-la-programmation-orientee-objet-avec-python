
""" Definit les class d'outils """

class BoiteaOutil:
    
    def __init__(self, tools):
        """Intialise les outils"""

        self.tools = []

     
    def Add_tools (self, tool):
        """ Ajouetr un outil """
        
        pass

    def remove_tools(self, tool):
        """ Retirer un outil """

        pass
        



class Marteau:

    def __init__(self, couleur="red"):
        """ Initialise la couleur """

        self.couleur = couleur



    def pain(self, couleur):
        """ Pain un marteau """

        pass


    def plante_clou(self, clou):
        """ enfonce un clou """

        pass
    
    def retirer_clou(self, clou):
        """ Retire un clou """

        pass




class Tounevisse:

    def __init__(self, taille):
        """ Initialise la taille d'une vis """

        self.taille = taille

    def serrer_vise(self, vis):
        """ Serrer une vis """

        pass

    
    def desserer_vise(self, vis):
        """ desserer une vis"""

        pass
