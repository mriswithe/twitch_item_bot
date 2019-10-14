from abc import ABC



class BaseItem(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self._description = description

    @property
    def description(self):
        return f'{self.name}: {self._description}'

    def __repr__(self):
        return f'{type(self).__name__}: {self.name}'

    def __str__(self):
        return self.name


class StackingItem(BaseItem):
    def __init__(self, effects: dict, stacking_desc: str, **kwargs):
        super().__init__(**kwargs)
        self._effects = effects
        self._stacking_desc = stacking_desc

    def stacked_description(self, quantity):
        data = {'quantity': quantity}
        for effect, edict in self._effects.items():
            data[effect] = eval(edict.get('formula'))
        formatted = self._stacking_desc.format_map(data)
        return formatted


class NonStackingItem(BaseItem):
    pass
