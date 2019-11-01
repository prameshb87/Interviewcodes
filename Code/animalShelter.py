"""
Create Animal Shelter system where a Dog or Cat can be rescued, but only the oldest (earliest rescued animal) can be adopted.
You can choose if you want a Cat or a Dog (but only the earliest rescued animal can be adopted)
Implement functions - enqueue, dequeue_any, dequeue_cat, dequeue_dog
"""

class Animal:
  def __init__(self, name, order):
    self.name = name
    self.adoption_order = order

  def print_name(self):
    print(self.name, self.adoption_order, "I am an Animal")

class Dog(Animal):
  def print_name(self):
    print(self.name, self.adoption_order, "I am a Dog")

class Cat(Animal):
  def print_name(self):
    print(self.name, self.adoption_order, "I am a Cat")

class AnimalShelter:
  dogs,cats = [], []
  order = 0

  def enqueue(self, animal):
    if isinstance(animal, Cat):
      self.cats.append(animal)
    else:
      self.dogs.append(animal)

  def dequeue_any(self):
    if len(self.cats) == 0:
      return self.dogs.pop(0)
    if len(self.dogs) == 0:
      return self.cats.pop(0)
    return self.cats.pop(0) if self.cats[0].adoption_order < self.dogs[0].adoption_order else self.dogs.pop(0)

  def dequeue_cat(self):
    return self.cats.pop(0)

  def dequeue_dog(self):
    return self.dogs.pop(0)

d1, d2, d3 = Dog('dog1', 0), Dog('dog2', 2), Dog('dog1', 3)
c1, c2, c3 = Cat('cat1', 1), Cat('cat2', 4), Cat('cat1', 5)

animal_shelter = AnimalShelter()
animal_shelter.enqueue(d1)
animal_shelter.enqueue(c1)
animal_shelter.enqueue(d2)
animal_shelter.enqueue(d3)
animal_shelter.enqueue(c2)
animal_shelter.enqueue(c3)
print([(d.name, d.adoption_order) for d in animal_shelter.dogs])
print([(c.name, c.adoption_order) for c in animal_shelter.cats])

animal_shelter.dequeue_any().print_name() # should return dog1
animal_shelter.dequeue_any().print_name() # should return cat1
animal_shelter.dequeue_cat().print_name() # should return cat2
animal_shelter.dequeue_dog().print_name() # should return dog2
