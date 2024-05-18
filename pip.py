# class LanguageLearning:
#     def __init__(self, target_language, proficiency_level):
#         self.target_language = target_language
#         self.proficiency_level = proficiency_level
#         self.exercises = {}
#         self.quizzes = {}
#         self.progress = 0 
#         self.resources = {
#             "Beginner": ["Textbook: Beginner's Guide to " + target_language, "Online course: Introduction to " + target_language],
#             "Intermediate": ["Intermediate " + target_language + " Grammar Workbook", "Conversation Practice: " + target_language],
#             "Advanced": ["Comprehension passages" + target_language + " Read and anwser the set question to perfect" + target_language]
#         }

#     def add_exercise(self, topic, exercise):
#         if topic not in self.exercises:
#             self.exercises[topic] = []
#         else:
#             self.exercises[topic].append(exercise)

#     def add_quiz(self, topic, quiz):
#         if topic not in self.quizzes:
#             self.quizzes[topic] = []
#         else:
#             self.quizzes[topic].append(quiz)

#     def track_progress(self):
#         self.progress += 1

#     def recommend_resources(self):

#         if self.proficiency_level == "Beginner" and self.progress < 3:
#             return self.resources["Beginner"]
#         elif self.proficiency_level == "Intermediate" and self.progress < 6:
#             return self.resources["Intermediate"]
#         elif self.proficiency_level == "Advanced" and self.progress < 10:
#             return self.resources["Advanced"]
#         else:
#             return []

#     def take_exercise(self, topic):
#         self.track_progress()
#         print("You completed the exercise on", topic)

#     def take_quiz(self, topic):
#         self.track_progress()
#         print("You completed the quiz on", topic)

#     def upgrade_proficiency_level(self):
#         if self.progress >= 6:
#             if self.proficiency_level == "Beginner":
#                 self.proficiency_level = "Intermediate"
#                 print("Congratulations! You have been upgraded to Intermediate level.")
#             else:
#                 print("You are already at the highest proficiency level.")

# # Example

# learner1 = LanguageLearning("French", "Beginner")

# learner1.add_exercise("Vocabulary", "Match the French words with their meanings.")
# learner1.add_quiz("Grammar", "Conjugation quiz for regular French verbs.")

# learner1.take_exercise("Vocabulary")
# learner1.take_quiz("Grammar")
# print("Recommended resources:", learner1.recommend_resources())

# learner1.upgrade_proficiency_level() 
# print("Current proficiency level:", learner1.proficiency_level)


# learner2= LanguageLearning("English", "Intermediate")

# learner2.add_quiz("Vocabulary", "Multiple-choice quiz on common French words.")
# learner2.add_quiz("Grammar", "Conjugation quiz for regular French verbs.")
# learner2.take_exercise("Vocabulary")
# learner2.take_quiz("Grammar")
# print("Recommended resources:", learner2.recommend_resources())

# learner2.upgrade_proficiency_level()
# print("Current proficiency level:", learner2.proficiency_level)


# Define a class for Ankara fabric
class AnkaraFabric:
    def __init__(self):
        self.temperature = 25  # Default temperature not necessary
        self.mood = 'neutral'  # Default mood   not necessary
        self.designs = {
            'neutral': ['design1', 'design2', 'design3'],  # Design patterns for neutral mood
            'happy': ['design4', 'design5', 'design6'],    # Design patterns for happy mood
            'sad': ['design7', 'design8', 'design9']       # Design patterns for sad mood
        }

    # Update temperature and mood
    def update_data(self, temperature, mood):
        self.temperature = temperature
        self.mood = mood

    # Predict fabric design based on temperature and mood
    def predict_design(self):
        temperature_index = self.temperature // 10  # Divide temperature range into 10-degree intervals
        mood_designs = self.designs.get(self.mood, self.designs['neutral'])  # Use neutral designs if mood not found
        design_index = temperature_index % len(mood_designs)  # Use modulo to loop through designs
        return mood_designs[design_index]

# Example usage
fabric = AnkaraFabric()
fabric.update_data(30, 'happy')  # Update with temperature and mood data
print("Predicted design:", fabric.predict_design())  # Predict design
