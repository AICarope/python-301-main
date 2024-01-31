# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class PatientApplicationForm:
    def __init__(self, patient_name, patient_age, patient_gender, symptoms, previous_conditions, allergies):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_gender = patient_gender
        self.symptoms = symptoms
        self.previous_conditions = previous_conditions
        self.allergies = allergies

    def __str__(self):
        return (f"patient_name:{self.patient_name}")
        return (f"patient_age:{self.patient_age}")
        return (f"patient_gender: {self.patient_gender}")
        return (f"symptoms: {self.symptoms}")
        return (f"previous_conditions: {self.previous_conditions}")
        return (f"allergies: {self.allergies}")
    
#instantiate: activate the class, to create two objects for diferent patients   
mypatient = PatientApplicationForm (patient_name = "John", patient_age ="29", patient_gender = "M", symptoms = "fever", previous_conditions = "covid",
                                   allergies = "peanuts")

mypatient2 = PatientApplicationForm (patient_name = "Maria", patient_age ="99", patient_gender = "F", symptoms = "vomit", previous_conditions = "cancer",
                                   allergies = "peanuts")
print (f"patient_name:{self.patient_name}")
print (f"patient_age:{self.patient_age}")
print (f"patient_gender: {self.patient_gender}")
print (f"symptoms: {self.symptoms}")
print (f"previous_conditions: {self.previous_conditions}")
print (f"allergies: {self.allergies}")

#HELP this is printing strange


# Child class 1
class OutpatientForm(PatientApplicationForm):
    def __init__(self, patient_name, patient_age, patient_gender, symptoms, previous_conditions, allergies, appointment_date):
        super().__init__(patient_name, patient_age, patient_gender, symptoms, previous_conditions, allergies)
        self.appointment_date = appointment_date

    # Additional method specific to the outpatient form
    def schedule_appointment(self, new_date):
        self.appointment_date = new_date
        print(f"Appointment booked for {self.appointment_date}")

    # Override __init__method
    def schedule_appointment(self, new_date, reschedule_date):
        super().schedule_appointment(new_date)
        self.reschedule_date = reschedule_date



#HELP  i am in the rigth track? i get an error
        