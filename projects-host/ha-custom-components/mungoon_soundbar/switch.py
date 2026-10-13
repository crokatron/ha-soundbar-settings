from homeassistant.components.switch import SwitchEntity
from .entity import SoundbarEntity
from .controls import SWITCHES
async def async_setup_entry(hass,entry,add_entities):add_entities([Setting(entry,key,info[0]) for key,info in SWITCHES.items()])
class Setting(SoundbarEntity,SwitchEntity):
 _attr_icon='mdi:speaker'
 @property
 def is_on(self):return self.last_value
 def restore(self,value):
  if value in ('on','off'):self.last_value=value=='on'
 async def async_turn_on(self,**kwargs):await self.set_value(True)
 async def async_turn_off(self,**kwargs):await self.set_value(False)
