#!/usr/bin/python3

# Pizza Fun
# created by Lu 3/14/16
# 3AM-Black-Coffee-Self-Motivated-Fuled-Awesome-Pizza-Class-Extraveganza


class Pizza(object):

    def __init__(self, brands, sizes, tops):
        self._brand = brands
        self._size = sizes
        self._top = tops

    def setPizza(self, brandt, sizet, topt):
        self._brand = brandt
        self._size = sizet
        self._top = topt

    def getPizza(self):

        return self._brand + self._size + str(self._top)

    def calCost(self):

        # if i use self._top, when using the pizza store class, the total price will be returned
        # so if i use a temp variable Cost, then i should be able to return the origional amount of toppings
        # in the pizza store class.

        # temp variable to return the total cost of toppings,
        cost = self._top

        if self._brand == "Pizza Hut":

            if self._size == "small":
                cost = 10 + (cost * 1)
                return cost

            elif self._size == "large":
                cost = 14 + (cost * 3)

        else:
            if self._brand == "Domino\'s":

                if self._size == "small":
                    cost = 12 + (cost * 2)
                    return cost

                elif self._size == "large":
                    cost = 16 + (cost * 3)
                    return cost

        return cost

    # use the __str__ self method to return literal strings and instance variables, insead of the address in memory
    # without this, the adress in memory will print out. that way you can print out hte actual object and not need to print out
    # the actual class methods. such as print p1.getPizza()
    def __str__(self):
        return  ""           + self._brand  + "\n" + \
            "" 	         + self._size   + " Pizza" "\n" + \
            "Cost is "   + "$" + str(self.calCost())   + "\n" \

# Part B


class PizzaStore(object):

    def __init__(self, name):
        self._name = name
        self._orderList = []

    def add(self, s):
        self._orderList.append(s)

    def __str__(self):

        orderInfo = " "

        for i in range(len(self._orderList)):
            orderInfo = orderInfo + \
                "\n" + self._orderList[i]._size + " size, "          + \
                str(self._orderList[i]._top)    + " toppings" + ", " + \
                self._orderList[i]._brand + ";"

        return self._name + " Has recieved the following Order: " + orderInfo


def main():

    print("##### Part A #####")
    p1 = Pizza("Pizza Hut", "small", 3)
    print(p1)

    #print (p1.getPizza())
    #p1.setPizza("sadsadada","sadsada",3 )
    # print(p1.getPizza())
    #p3 = Pizza ("Pizza Hut", "large", 3)
    #print (p3)

    p2 = Pizza("Domino\'s", "large", 2)
    print(p2)

    #print (p2.getPizza())
    #p2.setPizza("::::::::::::::::::::::::;","sadsada",3 )
    # print(p2.getPizza())
    #p4 = Pizza("Domino\'s", "small", 2)
    # print(p4)

    print("##### Part B #####")
    s1 = PizzaStore("Pizza House")

    s1.add(p1)
    s1.add(p2)
    print(s1)

    # if returning the attribute method, inside getPizza(), top needs to be converte to a string, which wouldent make sense if we computate it
    # print(p3.getPizza())

main()
