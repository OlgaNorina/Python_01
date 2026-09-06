## Class
In Object-Oriented Programming (OOP), a **class** is a blueprint, template, or recipe used to create objects.
In your specific garden simulation context, the Plant class is the master blueprint that defines what a generic "plant" looks like and what it can do. 
It doesn't represent one single plant in your garden; instead, it defines the rules for all plants.

## Operations
In Python, these **operations** are implemented as methods inside a class.

## Attributes (The Characteristics)
In OOP, attributes are the variables inside a class that **store** data or **characteristics** about an object.

## Instantiated (The Creation Process)
To instantiate means to actually **create a real, concrete object** from your class blueprint.
When your prompt says "the class will be instantiated, then the attributes will be set to their specific values," 
it means you write code to bring a specific plant to life in Python's memory.

## Behaviors
In OOP, an object shouldn't just hold data (like height and age); it should also control its own behavior. By moving the **if/elif growth rules** inside the Plant class, the object itself decides how it changes when you tell it to grow(). This core OOP concept is called Encapsulation.

## Encapsulation
Encapsulation is one of the four core pillars of Object-Oriented Programming (OOP).At its simplest, encapsulation means bundling data (attributes) and the actions that modify that data (methods/behaviors) together inside a single unit—the class [EEAT].

## 1. Encapsulation (Инкапсуляция)
**What it means:** Bundling data (attributes) and the actions that modify that data (methods) together inside a single unit (a class), while hiding internal details from the outside world.
**In garden:** Instead of having separate loose variables for a plant's height and a separate function for growth, you wrap them both tightly inside the Plant class. The outside program doesn't manually touch plant.height = 30; it just calls plant.grow(), and the class updates itself.

## 2. Inheritance (Наследование)
**What it means:** Creating a new class (subclass) based on an existing class (parent class). The subclass automatically inherits all attributes and methods from the parent, allowing you to reuse code without rewriting it.
**In garden:** You create a general parent class called Plant that holds name, height, and age. Then, you create a subclass called Cactus(Plant). The Cactus automatically gets the name, height, and age attributes for free, but you can add custom cactus-only features to it (like tracking thorns).

## 3. Polymorphism (Полиморфизм)
**What it means:** The word means "many forms." It allows different classes to have methods with the exact same name but completely different internal logic. When you call the method, Python automatically executes the correct version based on the object type.
**In garden:** You have a list containing a Rose, a Sunflower, and a Cactus. You loop through them and call .grow() on each. Because of polymorphism, the Sunflower shoots up by 5cm, the Rose grows by 2cm, and the Cactus grows by 0.2cm. You used the exact same command (.grow()), but it took many forms depending on the plant.

## 4. Abstraction (Абстракция)
**What it means:** Hiding complex background logic and showing only the essential features to the user. It reduces complexity by letting you interact with a simple interface.
**In garden:** Think of your main program loop. When you run plant.simulate_day(), you don't need to see or care about the math, the if/else checks for water levels, or the data updates happening under the hood. You just press the "simulate" button, and it works. The complexity is abstracted away.


https://correction-page.vercel.app/
