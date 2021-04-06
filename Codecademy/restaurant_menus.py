class Menu:
   #white space in variable to be revised
  def __init__(self, name, items, start_time,end_time):
    self.name,self.items, self.start_time,self.end_time=name, items,start_time,end_time
  def __repr__(self):
    return "This is {} menu, it is available from {} to {}".format(self.name,self.start_time,self.end_time)
  def calculate_bill(self,purchased_items):
    self.purchased_items=purchased_items
    sum=0
    for key,value in self.items.items():
      for item in purchased_items:
        if item==key:
          sum+=self.items[key]
    return sum

brunch=Menu("brunch",{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},1100,1600)

early_bird=Menu("early_bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},1500,1800)
dinner=Menu("dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},1700,2300)
kids=Menu("kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},1100,2100)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))
#here we start our franchise code
class Franchise:
  def __init__(self,address,menus):
    self.address,self.menus=address,menus
  def __repr__(self):
    return "Our franchise is located at {}, you can choose from our menus: {}".format(self.address,menus)
  def available_menus(self,time):
    available_menus=[]
    for menu in self.menus:
      if time>=menu.start_time and time<=menu.end_time:
        available_menus.append(menu.items)
    return available_menus
menus=[brunch,early_bird,dinner,kids]   
flagship_store=Franchise("1232 West End Road",menus)
new_installment=Franchise("12 East Mulberry Street",menus)
flagship_store.available_menus(1500)
print(flagship_store)
#here we create businesses
class Business(Menu):
  def __init__(self,name,franchises):
    self.name,self.franchises=name,franchises

business_one=Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])
arepas_menu={
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_place=Franchise("189 Fitzgerald Avenue",arepas_menu)
arepa_business=Business("Take a' Arepa",arepas_place)

