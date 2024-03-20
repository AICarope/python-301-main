#Final Project:

#Background
   #ADHD stands for attention deficit hyperactivity disorder. It is a medical condition. A person with ADHD has differences in brain development and brain activity that affect attention, the ability to sit still, and self-control. Research shows that just identifying a calming activity can reduce anxiety.  Being aware of children’s feelings is the first step!

#Project
   #The Feelings Thermometer is a visual tool that helps children measure how they are doing emotionally and what steps they can take to shift their mood when ​things are getting tough.
   #The display_feelings_thermometer() function displays the menu of feelings.
   #There are separate functions for managing each feeling: manage_anger(), manage_scared(), manage_happiness(), and manage_sadness().
   #The main() function takes user input and calls the appropriate function based on the input.




# Define a function to display the feelings thermometer
def display_feelings_thermometer():
    print("ADHD stands for attention deficit hyperactivity disorder. It is a medical condition identified in kids and adults. A person with ADHD has differences in brain development and emotions control!") 
    print("Hi friend, welcome to the Feelings Thermometer!")
    print("1. Anger") 
    print(("\U0001F621"))
    print("2. Scared")
    print(("\U0001F628"))
    print("3. Happy")
    print(("\U0001F600"))
    print("4. Sad")
    print(("\U0001F625"))

# Define a function to provide strategies for managing anger
def manage_anger():
    print("Strategies for managing anger:")
    print("- Count to 10 before reacting")
    print("- Take deep breaths")
    print("- Go for a walk or do some exercise")
    print("- **visit this link: https://www.youtube.com/watch?v=IN5z4gNOVYg")

# Define a function to provide strategies for managing fear
def manage_scared():
    print("Strategies for managing fear:")
    print("- Relax and smile")
    print("- Practice deep breathing or meditation")
    print("- Challenge negative thoughts")
    print("- Talk to someone you trust about your fears")
    print("- **visit this link: https://www.youtube.com/watch?v=L4RUCksQ-lA")


# Define a function to provide strategies for managing happiness
def manage_happiness():
    print("Strategies for managing happiness:")
    print("- Enjoy nature")
    print ("- Practice gratitude")
    print("- Engage in activities you enjoy")
    print("- Share your happiness with others")
    print("- **visit this link: https://www.youtube.com/watch?v=T8wyxbPx18c")

# Define a function to provide strategies for managing sadness
def manage_sadness():
    print("Strategies for managing sadness:")
    print("- Please dance") 
    print ("-Talk to someone about your feelings")
    print("- Engage in self-care activities")
    print("- Seek professional help if needed")
    print("- **visit this link: https://www.youtube.com/watch?v=m1wIcwu2LqU")


# Main function to run the feelings thermometer
def main():
    display_feelings_thermometer()
    choice = input("Enter the number corresponding to your feeling: ")

    if choice == "1":
        manage_anger()
    elif choice == "2":
        manage_scared()
    elif choice == "3":
        manage_happiness()
    elif choice == "4":
        manage_sadness()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main function
main()
print("- Why fit in when you were born to stand out? -Dr. Seuss")
print(("\U0001F64F"))

