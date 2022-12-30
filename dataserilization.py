# pydantic modules
from models.DataModels.characters import Characters as Char
from models.DataModels.Films  import Film as Film
from models.DataModels.planets import Planet_ as Plan
from models.DataModels.species import Species_ as Spec
from models.DataModels.starship import Starship_ as Star
from models.DataModels.vehicle import Vehicle_ as Vehi

# resource classes
from resources.character import Characters
from resources.films import Film
from resources.planate import Planet
from resources.species import Species
from resources.vehicles import Vehicle
from resources.starship import Spaceship

if __name__ == "__main__":

    character_data = Characters().get_sample_data()
    character_data = Char(**character_data)

    breakpoint()
    film_data = Film().get_sample_data()
    film_data = Film(**film_data)

    planet_data = Planet().get_sample_data()
    planet_data = Plan(**planet_data)

    species_data = Species().get_sample_data()
    species_data = Spec(**species_data)

    starship_data = Spaceship().get_sample_data()
    starship_data = Star(**starship_data)

    vehicle_data = Vehicle().get_sample_data()
    vehicle_data = Vehi(**vehicle_data)