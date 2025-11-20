import os


class Dog:
    initialized = False  # class-level flag

    def __init__(self, name: str, breed: str, age: float):
        self.name = name
        self.breed = breed
        self.age = age
        """
        Freesound.org → “Golden Retriever bark”
        Pixabay Audio → “Dog Bark Golden Retriever”
        Zapsplat → “Golden Retriever barking”
        """
        self.bark_sound = "dog-barking.mp3"

        if not Dog.initialized:
            print("Dog class is being initialized for the first time.")
            desired_location_of_audio_file = (
                "/Volumes/Drive/code/Python/PythonProjects/python-for-ai/code"
            )
            if os.getcwd() != desired_location_of_audio_file:
                os.chdir(desired_location_of_audio_file)
                print(f"Changed working directory to: {desired_location_of_audio_file}")

            Dog.initialized = True
        else:
            print("Dog class has already been initialized.")

    def __str__(self):
        return f"Dog(Name: {self.name}, Breed: {self.breed}, Age: {self.age})"

    def bark(self):
        print("Woof!")
        full_path_to_song = os.getcwd() + "/" + self.bark_sound
        print(full_path_to_song)
        full_path_to_song = "afplay " + full_path_to_song
        print(full_path_to_song)
        os.system(full_path_to_song)


class GoldenRetriever(Dog):
    def __init__(self, name: str, age: float):
        super().__init__(name, "Golden Retriever", age)
        self.bark_sound = "golden_retriever.mp3"


class Labrador(Dog):
    def __init__(self, name: str, age: float):
        super().__init__(name, "Labrador", age)
        self.bark_sound = "labrador-dog-barking.mp3"


buddy = GoldenRetriever(name="Buddy", age=2)
print(buddy)
# print(f"Dog Name: {buddy.name}, Breed: {buddy.breed}, Age:{buddy.age}")
buddy.bark()

howdy = Labrador(name="Howdy", age=0.5)
print(howdy)
# print(f"Dog Name: {howdy.name}, Breed: {howdy.breed}, Age:{howdy.age}")
howdy.bark()
