# Working with sets
from pyscript import display, document

grade_7 = {'Franco Deocampo', 'Sebastian Uclaray'}
grade_8 = {'Keane Pacaña', 'Almakram Arbison'}
grade_9 = {'Isabelle Cabatu', 'Nathan Bautista'}
grade_10 = {'Bonnie Nubla', 'Alexa Agnote'}

def create_order(event):
    first = document.getElementById('first_name').value
    last = document.getElementById('last_name').value

    new_member = {f"{first} {last}"}
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member

    document.getElementById('results').innerHTML = ""
    display(f'Full list of all members: {master_set}', target='results')
    display(f'Total number of members: {len(master_set)}', target='results')