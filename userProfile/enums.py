from enum import Enum
from django.db import models


class UserChoice(Enum):
    IS_MENTOR = "Mentor"
    IS_MENTEE = "Mentee"

    @classmethod
    def choices(cls):
        
        return tuple((i.name, i.value) for i in cls)

# ----------------------------  COUNTY ENUMS ----------------------------------

class CountyChoice(Enum):
    ALAMEDA = "Alameda"
    CONTRACOSTA = "Contra Costa"
    MARIN = "Marin"
    NAPA = "Napa"
    SANFRAN = "San Francisco"
    SANMATEO = "San Mateo"
    SANTACLARA = "Santa Clara"
    SOLANO = "Solano"
    SONOMA = "Sonoma"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)



class AlamedaChoice(Enum):
    ALAMEDA = "Alameda"
    ALBANY = "Albany"
    BERKELY = "Berkely"
    DUBLIN = "Dublin"
    EMERYVILLE = "Emeryville"
    FREMONT = "Fremont"
    HAYWARD = "Hayward"
    LIVERMORE = "Livermore"
    NEWARK = "Newark"
    OAKLAND = "Danville"
    PIEDMONT = "Piedmont"
    PLEASANTON = "Pleasanton"
    SANLEANDOR = "San Leandor"
    UNIONCITY = "Union City"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class ContraCostaChoice(Enum):
    ANTIOCH = "Antioch"
    BRENTWOOD = "Brentwood"
    CLAYTON = "Clayton"
    CONCORD = "Concord"
    DANVILLE = "Danville"
    ELCERRITO = "El Cerrito"
    HERCULES = "Hercules"
    LAFAYETTE = "Lafayette"
    MARTINEZ = "Martinez"
    MORAGA = "Moraga"
    OAKLEY = "Oakley"
    ORINDA = "Orinda"
    PINOLE = "Pinole"
    PITTSBURG = "Pittsburg"
    PLEASANTHILL = "Pleasant Hill"
    RICHMOND = "Richmond"
    SANPABLO = "San Pablo"
    SANRAMON = "San Ramon"
    WANUTCREEK = "Wanut Creek"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class MarinChoice(Enum):
    BELVEDERE = "Belverde"
    CORTEMADERA = "Cortemadera"
    FAIRFAX = "Fairfax"
    LARKSPUR = "Lakspur"
    MILLVALLEY = "Mill Valley"
    NOVATO = "Novato"
    ROSS = "Ross"
    SANANSELMO = "San Anselmo"
    SANRAFAEL = "San Rafael"
    SAUSALITO = "Suasalito"
    TIBURON = "Tiburon"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class NapaChoice(Enum):
    AMERICANCANYON = "American Canyon"
    CALISTOGA = "Calistoga"
    NAPA = "Napa"
    STHELENA = "St Helena"
    YOUNTVILLE = "Yountville"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class SanMateoChoice(Enum):
    ATHERTON = "Atherton"
    BELMONT = "Brentwood"
    BRISBANE= "Clayton"
    BURLINGAME = "Concord"
    COLMA = "Danville"
    DALYCITY = "Antioch"
    EASTPALOALTO = "Brentwood"
    FOSTERCITY = "Clayton"
    HALFMOONBAY = "Concord"
    HILLSBOROUGH = "Danville"
    MENLOPARK = "Antioch"
    MILBRAE = "Brentwood"
    PACIFICA = "Clayton"
    PORTOLAVALLEY = "Concord"
    REDWOODCITY = "Danville"
    SANBRUNO = "Antioch"
    SANCARLOS = "Brentwood"
    SANMATEOCOUNTY = "Clayton"
    SOUTHSANFRAN = "South San Francisco"
    WOODSIDE = "Woodside"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class SantaClaraChoice(Enum):
    CAMPBELL = "Campbell"
    CUPERTINO = "Cupertino"
    GILROY = "Gilroy"
    LOSALTOS = "Los Altos"
    LOSALTOSHILLS = "Los Altos Hills"
    LOSGATOS = "Los Gatos"
    MILPITAS = "Milpitas"
    MONTESERENO = "Monte Sereno"
    MORGANHILL = "Morgan Hill"
    MOUNTAINVIEW = "Mountain View"
    PALOALTO = "Palo Alto"
    SANJOSE = "San Jose"
    SANTACLARA = "Santa Clara"
    SARATOGA = "Saratoga"
    SUNNYVALE = "Sunnyvale"
    
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class SolanoChoice(Enum):
    BENICIA = "Benicia"
    DIXON = "Dixon"
    FAIRFIELD = "Fairfield"
    RIOVISTA = "Rio Vista"
    SUISUNCITY = "Suisun City"
    VACAVILLE = "Vacaville"
    VALLEJO = "Vallejo"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

class SonomaChoice(Enum):
    CLOVERDALE = "Cloverdale"
    COTATI = "Cotati"
    HEALDSBURG = "Healdsburg"
    PETALUMA = "Petaluma"
    ROHNERTPARK = "Rohnert Park"
    SANTAROSA = "Santa Rosa"
    SEBASTOPOL = "Sabastopol"
    SONOMACOUNTY = "Sonoma County"
    WINDSOR = "Windsor"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


# -------------------------- END OF COUNTY ENUMS ----------------------------------

class GenderChoice(Enum):
    HE = "He/Him"
    SHE = "She/Her"
    THEY = "They/Them"
    OTHER = "Other"

    @classmethod
    def choices(cls):
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
        return tuple((i.name, i.value) for i in cls)




class TrackChoice(Enum):
    PROFDEV= "Professional Development"
    INTERVIEWSKILL = "Interviewing Skills" 
    NETWORKING = "Networking" 
    LEADERSHIP = "Leadership"
    PUBLICSPEAK = "Public Speaking" 
    TECHSKILL = "Technical Skills" 
    TIMEMANAGE = "Time Management" 
    RESEARCH = "Research" 
    TECHNOLOGY ="Technology" 
    COMMUNICATION = "Communication"
    PM = "Project Management"
    UPDATES = "Industry Updates" 

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)




class EthnicityChoice(Enum):
    CAUCASIAN = "Caucasian"
    LATINO = "Hispanic or Latino"
    BLACK = "Black or African American" 
    NATIVE = "Native American or American Indian"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
