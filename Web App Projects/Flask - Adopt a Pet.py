from flask import Flask
from helper import pets
app = Flask(__name__)
app.config['DEBUG'] = True

# Define home page
@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
  <li><a href="/animals/dogs">Dogs</a></li>
  <li><a href="/animals/cats">Cats</a></li>
  <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  '''

# Function to display list of pets for a given type
@app.route('/animals/<pet_type>')
def animals(pet_type):
  # Define basic structure for the animal type
  html = f""" 
    <h1>List of {pet_type}</h1>
    """
  # Add a list to display each individual animal in the animal type 
  html += "<ul>" 
  # Add each individual animal to the displayed list
  for i, pet in enumerate(pets[pet_type]):
    html += f"<li><a href='/animals/{pet_type}/{i}'>{pet['name']}</a></li>"
    i += 1
  # Close the list at the end of key:value pairs for given animal type
  html += "</ul>"
  return html

# Define individual pet page with an index for keys in dict, wrap as an int
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  # Access pets dict by pet_type and pet_id for the current pet 
  try:
    pet = pets[pet_type][pet_id]
  except (KeyError, IndexError):
    return "<h1>Pet not found</h1>"
  # Define the page structure and use dynamic calls to each piece of information for the given pet
  html = f"""
  <h1>{pet['name']}</h1>
  <img src="{pet['url']}" alt="{pet['name']}"/>
  <p>{pet['description']}</p>
  <ul>
    <li>Breed: {pet['breed']}</li>
    <li>Age: {pet['age']}</li>
  </ul>
  """
  return html