
""" Defintion sur les attribues """

""" il existe trois types d'attribues dans la POO python """
""" Attribut de classe """
""" Attribut d'instance """
""" Attribut static """

""" attribut de classe : sont des varibales definies au niveau de la classe """
""" juste après la definition du nom de classe """
""" on peut acceder aux attributs de classe sans instantiation de la classe """

""" Attribut d'instance : sont les variables definis au niveau du constructeur de la classe """
""" les variables precedées par le mot clef < self > """
""" Pour acceder à l'attribut d'instance, il est obligatoire d'instantier la classe"""

""" Les attributs statique  :  sont des attributs independant de la classe """
""" Seul les methodes peuvent être des attributs """


class Bird:
    """ les oiseaux """

    """ Ici on utilise deux arributs de classe """
    name = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, names):
        """ Les attributs definis ici sont des attributs d'instances """

        self.position = 1, 2
        self.names = names

        """ On accede à l'attribut de classe position avec self (c'est possible) """
        self.positions[self.position] = self.name



    """ declaration d'une methode de class """
    @classmethod
    def find_bird(cls, position):
        """ Retrouver un oiseu selon sa position donnée """
        if position in cls.positions:
            print(f"on n'a retrouvé  un {cls.positions[position]} !")
        
        return " on n'a rien trouvé !"


    @staticmethod
    def get_definition():
        """Donne la définition d'un oiseau."""
        return (
        "Animal (vertébré à sang chaud) au corps recouvert de plumes, "
        "dont les membres antérieurs sont des ailes et qui a un bec."
        )

print(Bird.get_definition())


# On peut acceder aux variables de classe sans instanciation

Bird.name
Bird.positions

print(Bird.find_bird((2, 5)))

# On instancie un oiseau

bird = Bird("mouette")

# On le retoruve avec la methode find_bird

print(Bird.find_bird((1,2)))



