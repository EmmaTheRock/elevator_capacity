import os
from peewee import *

os.remove("elevator.db")

db = SqliteDatabase("elevator.db")

class Run(Model):
    number = IntegerField()

    class Meta:
        database = db  # This model uses the "elevator.db" database.

class Trial(Model):
    owner = ForeignKeyField(Run, backref='trial')

    class Meta:
        database = db  # this model uses the "elevator.db" database

def create_tables(database):
    database.create_tables([Run, Trial])

def add_run_data(current_run):
    run_entry = Run(number=current_run)
    run_entry.save() # the current run is now stored in the database

def add_trial_data(current_trial):
    trial_entry = Trial(number=current_trial)
    trial_entry.save() # the current trial is now stored in the database
    # TODO: add more fields for trial?

def set_trial_owner(current_run, current_trial):
    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

    xx = Trial.create(owner= #TODO: up to here)

def show_someones_pets():
    # 1
    Person.get(Person.name == 'Grandma L.')

    for person in Person.select():
        print(person.name)

    # 2
    query = (Pet
             .select(Pet, Person)
             .join(Person)
             .where(Pet.animal_type == 'cat'))

    for pet in query:
        print(pet.name, pet.owner.name)

    # 3
    for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
        print(pet.name)


if __name__ == "__main__":
    db.connect()
    create_tables(db)
    uncle_bob, grandma, herb = add_data()
    update_data(grandma)
    bob_kitty, herb_fido, herb_mittens, herb_mittens_jr = set_pet_owners()
    delete_pet(herb_mittens)
    show_someones_pets()
    db.close()