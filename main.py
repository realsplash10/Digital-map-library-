class Map:
    def __init__(self, name, scale, publisher, year):
        self.name = name
        self.scale = scale
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.name}, Scale: {self.scale}, Publisher: {self.publisher}, Year: {self.year}"


class Atlas:
    def __init__(self, name, publisher, year, maps=None):
        self.name = name
        self.publisher = publisher
        self.year = year
        self.maps = maps or {}

    def add_map(self, map_obj):
        self.maps[map_obj.name] = map_obj

    def remove_map(self, map_name):
        if map_name in self.maps:
            del self.maps[map_name]
        else:
            print(f"Map '{map_name}' not found in the atlas.")

    def display_atlas(self):
        print(f"Atlas Name: {self.name}, Publisher: {self.publisher}, Year: {self.year}")
        for map_name, map_obj in self.maps.items():
            print(f" - {map_obj}")

# Example usage:
if __name__ == "__main__":
    map1 = Map("City Map", "1:10000", "Map Publisher Inc.", 2023)
    map2 = Map("Country Map", "1:500000", "Geo World Maps", 2022)

    atlas = Atlas("World Atlas", "Global Publishers", 2021)
    atlas.add_map(map1)
    atlas.add_map(map2)

    atlas.display_atlas()

    atlas.remove_map("City Map")
    atlas.display_atlas()
