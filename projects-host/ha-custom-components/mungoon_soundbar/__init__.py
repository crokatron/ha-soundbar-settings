"""Extra native controls using the existing SmartThings connection."""
import asyncio
from homeassistant.const import Platform
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from .controls import payload,accepted
DOMAIN='mungoon_soundbar'
PLATFORMS=[Platform.NUMBER,Platform.SELECT,Platform.SWITCH]
def discover(hass):
 found={}
 for entry in hass.config_entries.async_entries('smartthings'):
  data=getattr(entry,'runtime_data',None)
  for did,device in getattr(data,'devices',{}).items():
   caps=device.status.get('main',{});label=str(device.device.label or device.device.name)
   model=getattr(caps.get('ocf',{}).get('mnmo'),'value','')
   if {'audioVolume','execute'}<=set(caps) and ('soundbar' in label.lower() or str(model).upper().startswith('HW-Q')):
    found[did]={'parent':entry.entry_id,'name':label,'model':str(model)}
 return found
class Connection:
 def __init__(self,hass,entry):self.hass=hass;self.entry=entry;self.lock=asyncio.Lock()
 @property
 def parent(self):return self.hass.config_entries.async_get_entry(self.entry.data['parent'])
 @property
 def ready(self):return self.parent is not None and self.entry.data['device_id'] in getattr(getattr(self.parent,'runtime_data',None),'devices',{})
 async def send(self,key,value):
  args=payload(key,value)
  async with self.lock:
   if not self.ready:raise HomeAssistantError('The SmartThings soundbar connection is unavailable.')
   try:
    async with asyncio.timeout(30):
     token=await self.parent.runtime_data.client.refresh_token_function()
     async with async_get_clientsession(self.hass).post('https://api.smartthings.com/v1/devices/'+self.entry.data['device_id']+'/commands',headers={'Authorization':'Bearer '+token},json={'commands':[{'component':'main','capability':'execute','command':'execute','arguments':args}]}) as response:
      response.raise_for_status();result=await response.json()
     if not accepted(result):raise HomeAssistantError('Samsung did not accept that soundbar setting.')
   except HomeAssistantError:raise
   except Exception as error:raise HomeAssistantError('The soundbar setting was not confirmed. Check SmartThings and try again.') from error
async def async_setup_entry(hass,entry):
 entry.runtime_data=Connection(hass,entry)
 await hass.config_entries.async_forward_entry_setups(entry,PLATFORMS)
 return True
async def async_unload_entry(hass,entry):return await hass.config_entries.async_unload_platforms(entry,PLATFORMS)
