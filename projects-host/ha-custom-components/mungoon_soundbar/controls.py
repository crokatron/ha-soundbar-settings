"""Samsung advanced audio commands, with strict single-setting payloads."""
import math
PREFIX='x.com.samsung.networkaudio.'
MODES={'Standard':'standard','Surround':'surround','Game Pro':'game','Adaptive Sound':'adaptive sound'}
NUMBERS={'bass_level':('Bass / subwoofer level','woofer','woofer',-6,6),
 'center_level':('Center speaker level','channelVolume','Spk_Center',-6,6),
 'rear_level':('Rear speaker level','channelVolume','Spk_Rear',-6,6)}
SWITCHES={'bass_boost':('Bass boost','bassboost'),'night_mode':('Night mode','nightmode'),'voice_amplifier':('Voice amplifier','voiceamplifier')}
def payload(key,value):
 if key in NUMBERS:
  _,resource,field,low,high=NUMBERS[key]
  if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or not low<=value<=high or int(value)!=value:raise ValueError('Choose a whole-number level within the slider range.')
  body={PREFIX+'channelVolume':[{'name':field,'value':int(value)}]} if resource=='channelVolume' else {PREFIX+field:int(value)}
 elif key in SWITCHES:
  if not isinstance(value,bool):raise ValueError('Choose on or off.')
  resource='advancedaudio';body={PREFIX+SWITCHES[key][1]:int(value)}
 elif key=='sound_mode':
  if value not in MODES:raise ValueError('Choose one of the available sound modes.')
  resource='soundmode';body={PREFIX+'soundmode':MODES[value]}
 else:raise ValueError('Unknown soundbar setting.')
 return ['/sec/networkaudio/'+resource,body]
def accepted(result):
 rows=result.get('results') if isinstance(result,dict) else None
 return isinstance(rows,list) and len(rows)==1 and isinstance(rows[0],dict) and rows[0].get('status')=='COMPLETED'
