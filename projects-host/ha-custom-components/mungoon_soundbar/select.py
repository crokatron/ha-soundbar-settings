from homeassistant.components.select import SelectEntity
from .entity import SoundbarEntity
from .controls import MODES
async def async_setup_entry(hass,entry,add_entities):add_entities([Mode(entry,'sound_mode','Sound mode')])
class Mode(SoundbarEntity,SelectEntity):
 _attr_options=list(MODES)
 _attr_icon='mdi:surround-sound'
 @property
 def current_option(self):return self.last_value
 def restore(self,value):
  if value in MODES:self.last_value=value
 async def async_select_option(self,option):await self.set_value(option)
