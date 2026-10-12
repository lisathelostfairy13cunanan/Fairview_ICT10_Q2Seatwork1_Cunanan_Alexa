from pyscript import document, display

# list of AOT Cadet Corps members (i got this from google)
students = [
    "Eren Yeager",
    "Mikasa Ackerman",
    "Armin Arlert",
    "Jean Kirstein",
    "Sasha Blouse",
    "Connie Springer",
    "Historia Reiss",
    "Reiner Braun",
    "Bertholdt Hoover",
    "Annie Leonhart",
    "Levi Ackerman",
    "Hange Zoe",
    "Erwin Smith",
    "Marco Bott",
    "Ymir",
]


def verify(e):
    # Clear the old result
    document.getElementById("result-box").innerHTML = ""

    # Get the names from the input boxes
    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()

    # Put the first and last name together
    full_name = f"{first_name.title()} {last_name.title()}"

    # Check if either input is empty
    is_empty = first_name == "" or last_name == ""

    # Check if the name is in the student list
    is_member = full_name in students

    # Messages depending on the result
    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now obligated to dedicate your hearts in the Cadet Corps."
    ]

    # Handle empty inputs
    empty_messages = [
        messages[is_member],
        "Please enter both your first and last name."
    ]

    # Get the message to show
    result_message = empty_messages[is_empty]

    # Show the result
    display(result_message, target="result-box")