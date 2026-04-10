# Mitchell Fontaine
# CS-660

import json


# Load the JSON data
def load_data(filepath="catalog.json"):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}. Please ensure it is in the same directory.")
        return None


# Part One: Recursion with Exception Handling
def get_innermost_leaves(data, target_key=None):
    # Recursively navigates a nested data structure to extract innermost leaf data.

    leaves = []
    
    try:
        # Manage invalid inputs explicitly
        if data is None:
            raise ValueError("Invalid input: Data cannot be None.")

        # Process structured data (dictionaries)
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    # Recursive call for nested structures
                    leaves.extend(get_innermost_leaves(value, target_key))
                else:
                    # Innermost leaf data reached
                    if target_key is None or key == target_key:
                        leaves.append(value)
                        
        # Process structured data (lists)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    # Only recurse if the item in the list is another list or dict
                    leaves.extend(get_innermost_leaves(item, target_key))
                else:
                    # If it's a primitive (like the "nitrogen" string) and we aren't 
                    # looking for a specific key, add it to the leaves
                    if target_key is None:
                        leaves.append(item)
                
        # Handle primitive data types passed directly
        else:
            if target_key is not None:
                # Triggers only when the user incorrectly calls the function on a primitive directly
                raise TypeError(f"Expected a dictionary or list, but got {type(data).__name__}.")
            leaves.append(data)

    except ValueError as ve:
        print(f"ValueError Handled: {ve}")
    except TypeError as te:
        print(f"TypeError Handled: {te}")
    except Exception as e:
        print(f"An unexpected error occurred during recursion: {e}")

    return leaves

# Part Two:

def process_astronomical_data(data_collection, processing_function):
    try:
        # Use Python's built-in function 'filter' to apply the passed function to the dataset.
        processed_data = list(filter(processing_function, data_collection))
        return processed_data
    except Exception as e:
        print(f"Error processing data functionally: {e}")
        return []


# Execution
if __name__ == "__main__":
    # Load the dataset
    catalog_data = load_data("catalog.json")
    
    if catalog_data:
        print("--- PART ONE: Recursion & Exception Handling ---")
        
        # Valid recursive extraction: Find all names in the entire catalog
        all_names = get_innermost_leaves(catalog_data, target_key="name")
        print(f"Found {len(all_names)} 'name' leaf nodes. First 5: {all_names[:5]}")
        
        # Invalid input handling: Passing None
        print("\nTesting invalid input handling (None):")
        get_innermost_leaves(None)
        
        # Invalid structure handling: Searching for a key in a primitive string
        print("\nTesting structured data exception handling (Primitive String):")
        get_innermost_leaves("This is a string, not a dict", target_key="name")


        print("\n--- PART TWO: Functional Constructs ---")
        
        # Extract a flat list of exoplanets to process
        exoplanet_systems = catalog_data["astronomical_catalog"].get("exoplanet_systems", [])
        all_exoplanets = []
        for system in exoplanet_systems:
            all_exoplanets.extend(system.get("planets", []))
            
        print(f"Total exoplanets loaded: {len(all_exoplanets)}")

        # Apply an anonymous function (lambda) to manipulate the data set
        # We will use the lambda to filter only planets that are in the habitable zone
        habitable_planets = process_astronomical_data(
            all_exoplanets, 
            lambda planet: planet.get("habitable_zone") is True
        )
        
        print("\nHabitable Planets Found (using lambda and higher-order function):")
        for p in habitable_planets:
            print(f"- {p['name']} (Radius: {p['radius_earth_radii']} Earth radii)")