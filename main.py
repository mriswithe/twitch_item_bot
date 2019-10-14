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