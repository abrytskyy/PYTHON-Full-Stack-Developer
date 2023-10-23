#Search for information about marine life:
ocean_ecosystem = {
    "fish": [
        {
            "name": "tuna",
            "maximum size (cm)": 200,
            "habitat": "pelagic",
            "diet": ["small fish", "squid"],
            "threat status": "vulnerable"
        },
        {
            "name": "shark",
            "maximum size (cm)": 700,
            "habitat": "pelagic and coastal",
            "diet": ["marine mammals", "fish"],
            "threat status": "critically endangered"
        },
        # Add other fish species
    ],
    "marine animals": [
        {
            "name": "blue whale shark",
            "maximum size (cm)": 1300,
            "habitat": "pelagic",
            "diet": ["fish", "marine birds"],
            "threat status": "vulnerable"
        },
        {
            "name": "jellyfish",
            "maximum size (cm)": 30,
            "habitat": "coastal and open waters",
            "diet": ["plankton", "fish"],
            "threat status": "low risk"
        },
        # Add other marine animal species
    ],
    "plants": [
        {
            "name": "corals",
            "type": "stony",
            "habitat": "coral reefs",
            "threat status": "vulnerable"
        },
        {
            "name": "seaweeds",
            "type": "green, red, brown",
            "habitat": "coastal and open waters",
            "threat status": "low risk"
        },
        # Add other plant species
    ]
}
# #1. Write a function that returns information about a marine animal or fish based on its name from the ocean ecosystem.
def marine_animal_or_fish(ecosystem ,name):
    for value in ecosystem.values():
        for type in value:
            if type["name"] == name:
                return type
print(marine_animal_or_fish(ocean_ecosystem, "corals"))
#
#
#
# #2. Finding the longest fish: Write a function that finds the longest fish in the ocean ecosystem and returns
# # its name and size.
def longest_fish(ecosystem):
    max_size = 0
    name = None
    for list_species in ecosystem.values():
        for species in list_species:
            if "maximum size (cm)" in species and species["maximum size (cm)"] > max_size:
                max_size = species["maximum size (cm)"]
                name = species["name"]
    return (name, max_size)
print(longest_fish(ocean_ecosystem))
# #
#
# #3. Filtering by threat status: Create a function that filters the list of marine species and fish based on a
# # specified threat status (e.g., "vulnerable") and returns the filtered list.
def filtering_by_threat_status(ecosystem, threat_status):
    for key, value in ecosystem.items():
        for type in value:
            if type["threat status"] == threat_status:
                print(type)
filtering_by_threat_status(ocean_ecosystem, "vulnerable")
#
#
#
# #4. Average fish size in a given location: Write a function that takes a habitat (e.g., "pelagic") and calculates
# #the average size of fish inhabiting that location.
def average_fish_by_location(ecosystem,habitat):
    list_sizes = []
    for list_species in ecosystem.values():
        for species in list_species:
            if species["habitat"] == habitat:
                list_sizes.append(species["maximum size (cm)"])
    avarage_size = sum(list_sizes)/ len(list_sizes)
    return avarage_size
print(average_fish_by_location(ocean_ecosystem, "pelagic"))

#
#
# #5. Information update: Implement a function that allows you to update information about a specific marine species
# or fish, such as their threat status.
def update_species_threat_status(category, name, new_status):
    for species in ocean_ecosystem[category]:
        if species["name"] == name:
            species["threat status"] = new_status
update_species_threat_status("plants", "corals", "low risk")
#
# print(ocean_ecosystem["plants"][0])
#
#
# #6. Counting species in categories: Write a function that counts the number of fish, marine animals,
# and plants in the ocean ecosystem.
def count_species():
    counts = {}
    for category, species_list in ocean_ecosystem.items():
        counts[category] = len(species_list)
    return counts
print(count_species())
#
# #7. Comparing the sizes of fish and marine animals: Write a function that compares the average size of fish and
# marine animals and reports which of these categories has larger representatives.
def compare_sizes():
    avg_fish_size = sum(species["maximum size (cm)"] for species in ocean_ecosystem["fish"]) / len(ocean_ecosystem["fish"])
    avg_animal_size = sum(species["maximum size (cm)"] for species in ocean_ecosystem["marine animals"]) / len(ocean_ecosystem["marine animals"])
    if avg_fish_size > avg_animal_size:
        print("Fish has large representatives than marine animals.")
    else:
        print("Marine animals has large representatives than fish.")
#
#
#
# #8. Threat assessment for species in a given location: Create a function that takes a habitat and outputs a list of
# # marine species and fish that inhabit that location, along with their threat statuses.

def species_in_habitat(habitat):
    species_list = []
    for category, species_data in ocean_ecosystem.items():
        for species in species_data:
            if species["habitat"].lower() == habitat.lower():
                species_list.append((species["name"], species["threat status"]))
    return species_list
print(species_in_habitat("pelagic"))

#9. Sorting by size: Write a function that sorts marine species and fish in the ocean ecosystem in descending order
# of their sizes.
def sort_species_by_size():
    sorted_species = {}
    for species_data in ocean_ecosystem.values():
        for species in species_data:
            if "maximum size (cm)" in species:
                sorted_species[species["name"]] = species["maximum size (cm)"]
    sorted_species = dict(sorted(sorted_species.items(), key=lambda item: item[1], reverse=True))
    return sorted_species

print(sort_species_by_size())


#10. Counting species diversity: Develop a function that counts how many different species of marine life and fish
# are present in the ocean ecosystem.

def count_species_diversity():
    unique_species = set()
    for species_data in ocean_ecosystem.values():
        for species in species_data:
            unique_species.add(species["name"])
    return len(unique_species)

print(count_species_diversity())
