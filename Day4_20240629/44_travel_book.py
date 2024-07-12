import pickle
from datetime import datetime

class Place:
    def __init__(self, name, latitude, longitude, visited_date):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.visited_date = visited_date

    def __str__(self):
        return f"{self.name}, Lat: {self.latitude}, Long: {self.longitude}, Visited: {self.visited_date}"

class TravelBook:
    def __init__(self, filename='travelbook.dat'):
        self.filename = filename
        self.places = self.load_places()

    def load_places(self):
        try:
            with open(self.filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []

    def save_places(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.places, file)

    def add_place(self, place):
        self.places.append(place)
        self.save_places()

    def display_places(self):
        if not self.places:
            print("No places in the travel book.")
        for place in self.places:
            print(place)

def main():
    travel_book = TravelBook()

    while True:
        print("\nTravel Book Menu:")
        print("1. Add a place")
        print("2. Display places")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter place name: ")
            latitude = float(input("Enter latitude: "))
            longitude = float(input("Enter longitude: "))
            visited_date = input("Enter visited date (YYYY-MM-DD): ")

            try:
                datetime.strptime(visited_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please enter date in YYYY-MM-DD format.")
                continue

            place = Place(name, latitude, longitude, visited_date)
            travel_book.add_place(place)
            print(f"Place '{name}' added to the travel book.")
        
        elif choice == '2':
            travel_book.display_places()

        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
