from homeassistant.components.number import NumberEntity,NumberMode
from .entity import SoundbarEntity
from .controls import NUMBERS
async def async_setup_entry(hass,entry,add_entities):add_entities([Level(entry,key,info) for key,info in NUMBERS.items()])
class Level(SoundbarEntity,NumberEntity):
 _attr_native_step=1
 _attr_mode=NumberMode.SLIDER
 _attr_icon='mdi:tune-vertical'
 def __init__(self,entry,key,info):
  super().__init__(entry,key,info[0]);self._attr_native_min_value=info[3];self._attr_native_max_value=info[4]
 @property
 def native_value(self):return self.last_value
 def restore(self,value):
  try:
   n=float(value)
   if self._attr_native_min_value<=n<=self._attr_native_max_value and int(n)==n:self.last_value=n
  except ValueError:pass
 async def async_set_native_value(self,value):await self.set_value(value)
