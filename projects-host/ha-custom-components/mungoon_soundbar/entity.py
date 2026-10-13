from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.helpers.entity import DeviceInfo
from . import DOMAIN
class SoundbarEntity(RestoreEntity):
 _attr_has_entity_name=True
 _attr_should_poll=False
 _attr_assumed_state=True
 def __init__(self,entry,key,name):
  self.connection=entry.runtime_data;self.key=key;self._attr_name=name
  self._attr_unique_id=entry.data['device_id']+'_'+key
  self._attr_device_info=DeviceInfo(identifiers={('smartthings',entry.data['device_id'])},name='Soundbar settings',model=entry.data.get('model') or None,manufacturer='Samsung Electronics',via_device=('smartthings',entry.data['device_id']))
  self._attr_extra_state_attributes={'state_source':'Last command accepted by Samsung; changes made in other apps or with the physical remote are not reported.','mungoon_soundbar_control':key}
  self.last_value=None
 @property
 def available(self):return self.connection.ready
 async def async_added_to_hass(self):
  await super().async_added_to_hass();state=await self.async_get_last_state()
  if state and state.state not in ('unknown','unavailable'):self.restore(state.state)
 def restore(self,value):self.last_value=value
 async def set_value(self,value):
  await self.connection.send(self.key,value);self.last_value=value;self.async_write_ha_state()
