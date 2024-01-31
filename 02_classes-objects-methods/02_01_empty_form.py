# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.


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

print(mypatient.patient_gender)
print(mypatient.patient_age)
print(mypatient2.symptoms)
print(mypatient2.patient_age)


