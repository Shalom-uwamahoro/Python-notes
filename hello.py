# def hello():
#     print("Helo Akirachix") #this is what idented means, we don't use curly brackets as other languages

# def hello(name):
#     print(f"Hello {name}")

# def year_of_birth(name,age):
#     print(f"Hello{name},  you were born in {2024-age}")# def should always start at the beginning of the line

# def my_country(country="Uganda"):
#     print(f"Hello AkiraChix from {country}")

# def greet(name):
#     print(f"Hello {name}")

# #creating a function that accepts any number of arguments
    
# def greet(*names):   # *name is by default converted to a list arguments, thus we can loop through it
#     for name in names:
#          print(f"Hello {name}")


# You are required to build a system to assist language learners in improving their language proficiency level. Your system must allow learners to:
# Input their target language and their language proficiency level.
# The system should, in turn, give learners language exercises and quizzes.
#  Additionally,
# Learners should be able to track their progress and have access to additional resources.


class LanguageLearning:
    def __init__(self, target_language, proficiency_level):
        self.target_language = target_language
        self.proficiency_level = proficiency_level
        self.exercises = {}
        self.quizzes = {}
        self.progress = 0 
        self.resources = {
            "Beginner": ["Textbook: Beginner's Guide to " + target_language, "Online course: Introduction to " + target_language],
            "Intermediate": ["Intermediate " + target_language + " Grammar Workbook", "Conversation Practice: " + target_language],
            "Advanced": ["Comprehension passages" + target_language + " Read and anwser the set question to perfect" + target_language]
        }

    def add_exercise(self, topic, exercise):
        if topic not in self.exercises:
            self.exercises[topic] = []
        else:
            self.exercises[topic].append(exercise)

    def add_quiz(self, topic, quiz):
        if topic not in self.quizzes:
            self.quizzes[topic] = []
        else:
            self.quizzes[topic].append(quiz)

    def track_progress(self):
        self.progress += 1

    def recommend_resources(self):

        if self.proficiency_level == "Beginner" and self.progress < 3:
            return self.resources["Beginner"]
        elif self.proficiency_level == "Intermediate" and self.progress < 6:
            return self.resources["Intermediate"]
        elif self.proficiency_level == "Advanced" and self.progress < 10:
            return self.resources["Advanced"]
        else:
            return []

    def take_exercise(self, topic):
        self.track_progress()
        print("You completed the exercise on", topic)

    def take_quiz(self, topic):
        self.track_progress()
        print("You completed the quiz on", topic)

    def upgrade_proficiency_level(self):
        if self.progress >= 6:
            if self.proficiency_level == "Beginner":
                self.proficiency_level = "Intermediate"
                print("Congratulations! You have been upgraded to Intermediate level.")
            else:
                print("You are already at the highest proficiency level.")

# Example

learner1 = LanguageLearning("French", "Beginner")

learner1.add_exercise("Vocabulary", "Match the French words with their meanings.")
learner1.add_exercise("Comprehension of passages", "Fill in the blanks with the correct verb forms.")
learner1.add_quiz("Vocabulary", "Multiple-choice quiz on common French words.")
learner1.add_quiz("Grammar", "Conjugation quiz for regular French verbs.")

learner1.take_exercise("Vocabulary")
learner1.take_quiz("Grammar")

print("Recommended resources:", learner1.recommend_resources())

learner1.upgrade_proficiency_level()
learner1.upgrade_proficiency_level()  

print("Current proficiency level:", learner1.proficiency_level)


learner2= LanguageLearning("English", "Intermediate")

learner2.add_exercise("Vocabulary", "Match the French words with their meanings.")
learner2.add_exercise("Comprehension of passages", "Fill in the blanks with the correct verb forms.")
learner2.add_quiz("Vocabulary", "Multiple-choice quiz on common French words.")
learner2.add_quiz("Grammar", "Conjugation quiz for regular French verbs.")

learner2.take_exercise("Vocabulary")
learner2.take_quiz("Grammar")

print("Recommended resources:", learner2.recommend_resources())

learner2.upgrade_proficiency_level()
learner2.upgrade_proficiency_level()  

print("Current proficiency level:", learner2.proficiency_level)
