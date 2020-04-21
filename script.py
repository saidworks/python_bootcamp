#Data : define variables
destinations=['Paris,France','Shanghai, China',"Los Angeles, USA",'São Paulo, Brazil','Cairo, Egypt']
test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
#functions 
def get_destination_index(destination):
  destination_index=0
  for i in range(len(destinations)):
    if destinations[i]==destination:
      destination_index=i
      return destination_index
def get_traveler_location(traveler):
  traveler_destination=""
  traveler_destination_index=destination_index
  return  traveler_destination_index
  
  
