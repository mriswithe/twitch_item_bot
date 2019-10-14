import yaml
import bot_item_classes as bic

with open('items.yaml') as fp:
    items = yaml.safe_load(fp)

created_items = {}
for item in items:
    classref = getattr(bic, item.get('class'))
    created_items[item.get('name')] = classref(name=item.get('name'), description=item.get('description'),
                                               effects=item.get('effects'), stacking_desc=item.get('stacking_desc'))
syringe = created_items.get('Soldier\'s Syringe')

print(syringe.description)
print(syringe.stacked_description(5))

teddy = created_items.get('Tougher Times')
print(teddy)
print(teddy.description)
print(teddy.stacked_description(1))
print(teddy.stacked_description(5))
print(teddy.stacked_description(10))

scythe = created_items.get('Harvester\'s Scythe')
print(scythe)
print(scythe.description)
print(scythe.stacked_description(1))
print(scythe.stacked_description(5))
print(scythe.stacked_description(10))
print(scythe.stacked_description(15))