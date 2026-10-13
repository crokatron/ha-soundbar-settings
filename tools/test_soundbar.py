import importlib.util, math, unittest
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'projects-host/ha-custom-components/mungoon_soundbar/controls.py'
s=importlib.util.spec_from_file_location('controls',p);c=importlib.util.module_from_spec(s);s.loader.exec_module(c)
class SoundbarTests(unittest.TestCase):
 def test_each_setting_produces_one_supported_request(self):
  for key,value in [('bass_level',-6),('center_level',6),('rear_level',0),('bass_boost',True),('night_mode',False),('voice_amplifier',True),('sound_mode','Standard')]:
   path,body=c.payload(key,value);self.assertTrue(path.startswith('/sec/networkaudio/'));self.assertEqual(len(body),1)
 def test_invalid_requests_are_rejected(self):
  for key,value in [('bass_level',7),('center_level',-7),('rear_level',1.5),('rear_level',True),('rear_level',math.nan),('night_mode','yes'),('sound_mode','unknown'),('unknown',1)]:
   with self.assertRaises(ValueError):c.payload(key,value)
 def test_only_single_confirmed_result_is_accepted(self):
  self.assertTrue(c.accepted({'results':[{'status':'COMPLETED'}]}))
  for value in [{},None,{'results':[]},{'results':[{'status':'FAILED'}]},{'results':[{'status':'COMPLETED'},{'status':'COMPLETED'}]}]:self.assertFalse(c.accepted(value))
if __name__=='__main__':unittest.main()
