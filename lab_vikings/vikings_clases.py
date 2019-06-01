# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # add code here
    pass

    def attack(self):
        return self.strength

    def receive_damage(self,damage):
        self.health -= damage


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receive_damage(self,damage):
        self.health -= damage
        if self.health > 0:
            return(self.name+" has received "+str(damage)+" points of damage")
        elif self.health <= 0:
            return(self.name+" has died in act of combat")

    def battle_cry(self):
        return "Odin Owns You All!"



# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self,damage):
        self.health -= damage
        if self.health > 0:
            return("A Saxon has received "+str(damage)+" points of damage")
        elif self.health <= 0:
            return("A Saxon has died in combat")

# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self,viking):
        self.viking_army.append(viking)

    def add_saxon(self,saxon):
        self.saxon_army.append(saxon)

    def viking_attack(self):
        anysaxon = random.randrange(len(self.saxon_army)) #ramdom.choise???
        anyviking = random.randrange(len(self.viking_army))
        selectedsaxon = self.saxon_army[anysaxon]
        selectedviking = self.viking_army[anyviking]


        message = selectedsaxon.receive_damage(selectedviking.strength)
        if message == "A Saxon has died in combat":
            self.saxon_army.pop(anysaxon)
        return message

    def saxon_attack(self):
        anysaxon = random.randrange(len(self.saxon_army)) #ramdom.choise???
        anyviking = random.randrange(len(self.viking_army))
        selectedsaxon = self.saxon_army[anysaxon]
        selectedviking = self.viking_army[anyviking]


        message = selectedviking.receive_damage(selectedsaxon.strength)
        if message == "A Saxon has died in combat":
            self.saxon_army.pop(anysaxon)
        return message

    def show_status(self):
        if len(self.saxon_army) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.viking_army) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif (len(self.viking_army) >= 1) and (len(self.saxon_army) >= 1):
            return "Vikings and Saxons are still in the thick of battle."





"""
Now we get to the good stuff: WAR! Our War constructor function will allow us to have a Viking army and a Saxon army that battle each other.

Modify the War constructor and add 5 methods to its prototype:

add_viking()
add_saxon()
viking_attack()
saxon_attack()
show_status()
constructor function
When we first create a War, the armies should be empty. We will add soldiers to the armies later.

should receive 0 arguments
should assign an empty array to the viking_army property
should assign an empty array to the saxon_army property
add_viking() method
Adds 1 Viking to the viking_army. If you want a 10 Viking army, you need to call this 10 times.

should be a function
should receive 1 argument (a Viking object)
should add the received Viking to the army
shouldn't return anything
add_saxon() method
The Saxon version of add_viking().

should be a function
should receive 1 argument (a Saxon object)
should add the received Saxon to the army
shouldn't return anything

viking_attack() method
A Saxon (chosen at random) has their receive_damage() method called with the damage equal to the strength of a Viking (also chosen at random). 
This should only perform a single attack and the Saxon doesn't get to attack back.

should be a function
should receive 0 arguments
should make a Saxon receive_damage() equal to the strength of a Viking
should remove dead saxons from the army
should return result of calling receive_damage() of a Saxon with the strength of a Viking
saxonAttack() method
The Saxon version of viking_attack(). A Viking receives the damage equal to the strength of a Saxon.

should be a function
should receive 0 arguments
should make a Viking receive_damage() equal to the strength of a Saxon
should remove dead vikings from the army
should return result of calling receive_damage() of a Viking with the strength of a Saxon
showStatus() method
Returns the current status of the War based on the size of the armies.

should be a function
should receive 0 arguments
if the Saxon array is empty, should return "Vikings have won the war of the century!"
if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."   
    
"""
