from enum import Enum
from django.db import models


class UserChoice(Enum):
    IS_MENTOR = "MENTOR"
    IS_MENTEE = "MENTEE"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)



class CountyChoice(Enum):
    SONOMA = "Sonoma"
    NAPA = "Napa"
    SOLANO = "Solano"
    CONTRACOSTA = "Contra Costa"
    ALAMEDA = "Alameda"
    SANTACLARA = "Santa Clara"
    SANMATEO = "San Mateo"
    SANFRAN = "San Francisco"
    MARIN = "Marin"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)



class GenderChoice(Enum):
    HE = "He/Him"
    SHE = "She/Her"
    THEY = "They/Them"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)

class EducationChoice(Enum):
    HIGHSCHOOL = "High School"
    SOMECOLLEGE = "Some College"
    ASSOCIATES = "Associates"
    BACHELORS = "Bachelors"
    MASTERS = "Masters"
    DOCTORAL = "Doctoral"


    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)


class IndustryChoice(Enum):
    DATING = "dating"
    DIY = "DIY"
    ECOMERCE="e-commerce/delivery"
    EDUCATION ="education"
    ENERGY= "energy"
    ENTERPRISE = "enterprise"
    FASHBEAU = "fashion & beauty"
    FINANCE = "finance"
    FOOD = "food"
    GAMING = "gaming"
    GOVTANDPOL = "Government and Politics"
    HEALTH = "Health and Wellness"
    INTERIORDESIGN = "Interior Design"
    MARKETING = "Marketing"
    MEDIA = "Media and Entertainment"
    MESSAGING = "Messaging"
    MUSIC = "Music"
    NONPROFIT = "Nonprofit"
    PAYMENT = "Payment"
    REALESTATE = "Real Estate"
    RETAIL = "Retail"
    SOCIALNET = "Social Network"
    SPORTS = "Sports"
    TECH = "Technology"
    TELECOM = "Telecommunications"
    TRANSPORTATION = "Transportation"
    TRAVEL = "Travel"
    VENCAP = "Venture Capital"
    WEARABLES = "Wearables"


    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
