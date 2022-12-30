"""
TODO
1. pull data for the movie "A New Hope" and save in DB
2. Replace the data for each of the endpoint listed in the JSON object
 and insert that data into respective database tables
 (using following instructions)
    (For example - "A New Hope" has following resource endpoints)
        - characters
        - planets
        - vehicles
        - starships
        - species
3. Convert height and weight in each character to standard units
4. You have to remove all cross-referencing URLs from each resource
"""

# pydantic models
from models.DataModels.characters import Characters
from models.DataModels.Films import Film as Films_
from models.DataModels.planets import Planet_
from models.DataModels.species  import Species_
from models.DataModels.starship import Starship_
from models.DataModels.vehicle import Vehicle_

# resource-classes
# from Resources.planets import Planets
from resources.films import Film
# from Resources.characters import Characters
# from Resources.vehicles import Vehicles
# from Resources.species import Species
# from Resources.spaceships import Spaceships

from dal.dml import insert_resource
from utils.fetch_data import fetch_data

if __name__ == "__main__":

    film_data = Films_().get_sample_data(id_=1)
    film_data = Films_(**film_data)

    film_columns = [
        "title",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]

    film_values = [
        film_data.title,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )

    # character data
    character = fetch_data(film_data.characters)
    character_counter = 1
    for characters in character:
        chracter_data = character(**characters)

        character_columns = [
            "name",
            "height",
            "mass",
            "hair_color",
            "skin_color",
            "eye_color",
            "birth_year",
            "gender",
            "homeworld"
        ]
        character_values = [
            chracter_data.name,
            chracter_data.height,
            chracter_data.mass,
            chracter_data.hair_color,
            chracter_data.skin_color,
            chracter_data.eye_color,
            chracter_data.birth_year,
            chracter_data.gender,
            chracter_data.homeworld

        ]
        result = insert_resource(
            "characters", "char_id", character_counter, character_columns, character_values)
        character_counter += 1

    # planets data
    planets = fetch_data(film_data.planets)
    planets_counter = 1
    for planet in planets:
        planet_data = Planet_(**planet)

        planet_colums = [
            "climate",
            "diameter",
            "gravity",
            "name",
            "orbital_period",
            "population",
            "rotation_period",
            "surface_water",
            "terrain"
        ]

        planet_values = [
            planet_data.climate,
            planet_data.diameter,
            planet_data.gravity,
            planet_data.name,
            planet_data.orbital_period,
            planet_data.population,
            planet_data.rotation_period,
            planet_data.surface_water,
            planet_data.terrain
        ]
        result = insert_resource(
            "planet", "planet_id", planets_counter, planet_colums, planet_values)
        planets_counter += 1

    # vehicles data
    vehicles = fetch_data(film_data.vehicles)
    vehicles_counter = 1
    for vehicle in vehicles:
        vehicle_data = Vehicle_(**vehicle)

        vehicle_colums = [
            "cargo_capacity",
            "consumables",
            "cost_in_credits",
            "crew",
            "length",
            "manufacturer",
            "max_atmosphering_speed",
            "model",
            "name",
            "passengers",
            "vehicle_class",
        ]

        vehicle_values = [
            vehicle_data.cargo_capacity,
            vehicle_data.consumables,
            vehicle_data.cost_in_credits,
            vehicle_data.crew,
            vehicle_data.length,
            vehicle_data.manufacturer,
            vehicle_data.max_atmosphering_speed,
            vehicle_data.model,
            vehicle_data.name,
            vehicle_data.passengers,
            vehicle_data.vehicle_class
        ]
        result = insert_resource(
            "vehicle", "vehicle_id", vehicles_counter, vehicle_colums, vehicle_values)
        vehicles_counter += 1

    # starships data

    starships = fetch_data(film_data.starships)
    starships_counters = 1
    for starship in starships:
        starship_data = Starship_(**starship)

        starship_colums = [
            "MGLT",
            "cargo_capacity",
            "consumables",
            "cost_in_credits",
            "crew",
            "hyperdrive_rating",
            "length",
            "manufacturer",
            "max_atmosphering_speed",
            "model",
            "name",
            "starship_class",
            "passengers"
        ]

        starship_values = [
            starship_data.MGLT,
            starship_data.cargo_capacity,
            starship_data.consumables,
            starship_data.cost_in_credits,
            starship_data.crew,
            starship_data.hyperdrive_rating,
            starship_data.length,
            starship_data.manufacturer,
            starship_data.max_atmosphering_speed,
            starship_data.model,
            starship_data.name,
            starship_data.starship_class,
            starship_data.passengers
        ]

        result = insert_resource(
            "starship", "starship_id", starships_counters, starship_colums, starship_values)

        starships_counters += 1

    # species data
    species = fetch_data(film_data.species)
    species_counter = 1
    for specie in species:
        specie_data = Species_(**specie)

        specie_colums = [
            "average_height",
            "average_lifespan",
            "classification",
            "designation",
            "eye_colors",
            "hair_colors",
            "name",
            "skin_colors"
        ]
        specie_vlaue = [
            specie_data.average_height,
            specie_data.average_lifespan,
            specie_data.classification,
            specie_data.designation,
            specie_data.eye_colors,
            specie_data.hair_colors,
            specie_data.name,
            specie_data.skin_colors
        ]
        result = insert_resource(
            "species", "species_id", species_counter, specie_colums, specie_vlaue)
        species_counter += 1
