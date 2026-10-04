class Meal:
    def __init__(self):
        self.cost = 0.0
        self.takeOut = False
        self.main = ""
        self.drink = ""

    def getCost(self) -> float:
        return self.cost

    def setCost(self, cost: float) -> None:
        self.cost = cost

    def getTakeOut(self) -> bool:
        return self.takeOut

    def setTakeOut(self, takeOut: bool) -> None:
        self.takeOut = takeOut

    def getMain(self) -> str:
        return self.main

    def setMain(self, main: str) -> None:
        self.main = main

    def getDrink(self) -> str:
        return self.drink

    def setDrink(self, drink: str) -> None:
        self.drink = drink


class MealBuilder:
    
    def __init__(self):
        self.currCost = 0
        self.takeOut = None
        self.mainCourses = []
        self.drink = []

    def addCost(self, cost: float) -> 'MealBuilder':
        self.currCost += cost

    def addTakeOut(self, takeOut: bool) -> 'MealBuilder':
        self.takeOut = takeOut

    def addMainCourse(self, main: str) -> 'MealBuilder':
        self.mainCourses.append(main)

    def addDrink(self, drink: str) -> 'MealBuilder':
        self.drink.append(drink)

    def build(self) -> Meal:
        meal = Meal()
        meal.setCost(self.currCost)
        meal.setTakeOut(self.takeOut)
        meals = ", ".join(self.mainCourses)
        meal.setMain(meals)
        drinks = ", ".join(self.drink)
        meal.setDrink(drinks)
        return meal


