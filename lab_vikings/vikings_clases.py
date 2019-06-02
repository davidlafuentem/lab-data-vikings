# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # add code here

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
        self.health -= damage   #modelate a fight by substracting the damage from the health
        if self.health > 0:
            return(self.name+" has received "+str(damage)+" points of damage")
        elif self.health <= 0:  #if there isn't health, the viking is death
            return(self.name+" has died in act of combat")

    def battle_cry(self):
        return "Odin Owns You All!"



# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receive_damage(self,damage):
        self.health -= damage   #modelate a fight by substracting the damage from the health
        if self.health > 0:
            return("A Saxon has received "+str(damage)+" points of damage")
        elif self.health <= 0: #if there isn't healt, the saxon is death
            return("A Saxon has died in combat")

# War
class War:
    def __init__(self):
        self.viking_army = []
        self.saxon_army = []

    def add_viking(self,viking):
        self.viking_army.append(viking) #it receive an instance of the class Viking to be store in a list

    def add_saxon(self,saxon):
        self.saxon_army.append(saxon)   #it receive an instance of the class Saxon to be store in a list

    def viking_attack(self):
        anysaxon = random.randrange(len(self.saxon_army)) #select randomly one index from the entire list of saxons
        anyviking = random.randrange(len(self.viking_army)) #select randomly one index from the entire list of vikings
        selectedsaxon = self.saxon_army[anysaxon]   #select the saxon pointed with the selected index
        selectedviking = self.viking_army[anyviking]    #select the viking pointed with the selected index


        message = selectedsaxon.receive_damage(selectedviking.strength)
        if message == "A Saxon has died in combat":
            self.saxon_army.pop(anysaxon)
        return message

    def saxon_attack(self):
        anysaxon = random.randrange(len(self.saxon_army)) #ramdom.choise???
        anyviking = random.randrange(len(self.viking_army))
        selectedsaxon = self.saxon_army[anysaxon]
        selectedviking = self.viking_army[anyviking]

        message = selectedviking.receive_damage(selectedsaxon.strength) #message describes what happened in the fight
        #if message == self.name+" has died in act of combat": # ---- self.name seems to be out of the scope? ----
        if message.find("has died in act of combat") != -1:
            self.viking_army.pop(anyviking) #by context of message, seems that wiking has died, so we erase him from list
        return message

    def show_status(self):
        #if the Saxon array is empty, should return "Vikings have won the war of the century!"
        if len(self.saxon_army) < 1:
            return 'Vikings have won the war of the century!'
        #if the Viking array is empty, should return "Saxons have fought for their lives and survive another day..."
        elif len(self.viking_army) < 1:
            return 'Saxons have fought for their lives and survive another day...'
        #if there are at least 1 Viking and 1 Saxon, should return "Vikings and Saxons are still in the thick of battle."
        elif (len(self.viking_army) >= 1) and (len(self.saxon_army) >= 1):
            return "Vikings and Saxons are still in the thick of battle."
