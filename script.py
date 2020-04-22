#Data : define variables
destinations=['Paris, France','Shanghai, China',"Los Angeles, USA",'São Paulo, Brazil','Cairo, Egypt']
test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions=[ [] for i in range(len(destinations))]


#functions for getting informations from the traveler
def get_destination_index(destination):
  destination_index=0
  for i in range(len(destinations)):
    if destinations[i]==destination:
      destination_index=i
      return destination_index
def get_traveler_location(traveler):
  traveler_destination=destinations[1]
  traveler_destination_index=get_destination_index(destinations[1])
  return  traveler_destination_index
test_destination_index=get_traveler_location(test_traveler)

def add_attraction(destination,attraction):
  try:
    destination_index=get_destination_index(destination)
    attractions_for_destination=attractions[destination_index]
    attractions_for_destination.append(attraction)
  except SyntaxError:
    return
  
def find_attractions(destination,interests):
  destination_index=get_destination_index(destination)
  attractions_in_city=attractions[destination_index]
  attractions_with_interest=[]
  for attraction in attractions_in_city:
    possible_attraction=attraction
    attraction_tags=attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest  

def get_attractions_for_traveler(traveler):
  traveler_destination=traveler[1]
  traveler_interests=traveler[2]
  traveler_attractions=find_attractions(traveler_destination,traveler_interests)
  interests_string="Hi "+ traveler[0]
  interests_string += ", we think you'll like these places around "+ traveler_destination+": "
  for attraction in traveler_attractions:
    interests_string += attraction + ", "
  return interests_string  
  
  
  
    
  
#add attraction to locations
add_attraction('Los Angeles, USA',['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
la_arts=find_attractions("Los Angeles, USA",['art'])
print(la_arts)
smills_france=get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)