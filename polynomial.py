# from _typeshed import Self
from cmath import sqrt
import operator
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self,*coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.coeffs = list(coeffs)

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        resultat= list(map(operator.add,self.coeffs, other.coeffs)) 
        return Poly2(resultat)

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        
        resultat=  [x - y for x, y in zip(self.coeffs, other.coeffs)]
        return Poly2(list(resultat))

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        # c2 = "+" if self.coeffs[1] > 0 else ""
        # c3 = "+" if self.coeffs[2] > 0 else ""
        return f"{str(self.coeffs[0])}X^2 {str(c2)} {str(self.coeffs[1])}X {str(c3)}  {str(self.coeffs[2])} "

    # def solve(self):
    #     """ Méthode qui renvoie les solutions si elles existent."""
    #     pass

    # def __val(self, x):
    #     """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
    #     Si: y = x^2 + 1
    #     Si: x prend pour valeur 5
    #     Alors: y = 5^2 + 1 = 26
    #     """
    #     pass

    # def draw(self, x_points=None):
    #     """ Méthode qui trace la courbe, voir fichier png."""
    #     pass


if __name__ == "__main__":
    bar = [10, -5, 4]
    p1 = Poly2(*bar)
    print(p1)
    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    # print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    # p1.draw()  # trace la courbe de p1, voir fichier png
