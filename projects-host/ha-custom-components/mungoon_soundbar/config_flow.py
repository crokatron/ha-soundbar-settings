import voluptuous as vol
from homeassistant import config_entries
from . import DOMAIN,discover
class Flow(config_entries.ConfigFlow,domain=DOMAIN):
 VERSION=1
 async def async_step_user(self,user_input=None):
  choices=discover(self.hass)
  if not choices:return self.async_abort(reason='no_soundbar')
  if user_input is not None:
   did=user_input['device_id']
   if did not in choices:return self.async_abort(reason='no_soundbar')
   await self.async_set_unique_id(did);self._abort_if_unique_id_configured()
   info=choices[did]
   return self.async_create_entry(title=info['name'],data={'device_id':did,**info})
  return self.async_show_form(step_id='user',data_schema=vol.Schema({vol.Required('device_id'):vol.In({did:info['name'] for did,info in choices.items()})}))
