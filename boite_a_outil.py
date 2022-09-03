
""" Definit les class d'outils """

class BoiteaOutil:
    
    def __init__(self, tools):
        """Intialise les outils"""

        self.tools = []

     
    def Add_tools (self, tool):
        """ Ajouetr un outil """
        self.tools.append(tool)

    def remove_tools(self, tool):
        """ Retirer un outil """
        index = self.tools.index(tool)
        del self.tools[index]



class Marteau:

    def __init__(self, couleur="red"):
        """ Initialise la couleur """

        self.couleur = couleur


    def paint(self, couleur):
        """ Pain un marteau """

       self.couleur = couleur


    def planter_clou(self, clou):
        """ enfonce un clou """

        clou.nail_in()


    def retirer_clou(self, clou):
        """ Retire un clou """

        clou.remove()

    
    def __repr__(self):
        """ represenation de l'objet """
        return f"marteau de coleur {self.couleur}"


class Tounevisse:

    def __init__(self, taille):
        """ Initialise la taille d'une vis """

        self.taille = taille

    def serrer_vise(self, vis):
        """ Serrer une vis """

        vis.serrer()

    
    def desserer_vise(self, vis):
        """ desserer une vis"""

        vis.devisser()


    

class Clou:
    """ le clou"""

    def __init__(self):
        """ Initialisation de la position du clou dans le mure """

        self.in_wall = false

    def nail_in(self):
        """ plante le clou """

        if not self.in_wall:
            self.in_wall = True

    def remove():
        """ retire le clou """

        if self.in_wall:
            self.in_wall = False


    def __str__(self):
        """ retourne une forme lisible de clou """

        wall_stat = "le clou est dans le trou" if self.in_wall else "le clou n'est pas dans le trou"
        return f"le statut du clou {self.wall_stat}."


class Vis:
    """ vis"""

    MAX_NIVEAU = 5

    def __init__(self):
        """initialiser son dégré de serrage """

        self.tightness = 0


    def vis_serrer(self):
        """ serrer le vis """

        if self.tightness < 5 :
            self.tightness +=1

    def vis_desserer(self):
        """ deserrer le vis """

        if self.tightness > 5:
            self.tightness -=1
    

