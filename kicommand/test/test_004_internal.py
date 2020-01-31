import unittest
import pcbnew
import kicommand
from kicommand import run as kc

class TestInternal(unittest.TestCase):

    def test_pcbnew(self):
        self.assertEqual(kc('pcbnew'),pcbnew)
		
    def test_load(self):
        pcommands = ['moduletextobj', 'wxpoint', 'outlinetoptext', 'setselect', 'referencetextobj', 'outlinepads', 'valuetextobj', 'drawparams', 'textfromobj', 'referencetext', 'toptextobj', 'outlinetext', 'clearallselected', 'not', 'orthogonal', 'copy', 'clearselect', 'texttosegments', 'valuetext']
        self.assertTrue(set(pcommands) <= set(kicommand.kicommand._dictionary['persist'].keys()))
        self.assertFalse(set(['thiscommand doesnt exist']) < set(kicommand.kicommand._dictionary['persist'].keys()))

    def test_help_helpcat_explain_see_seeall(self):
        result = kc("clear help All helpcat 'help explain seeall 'bool see",returnval=-1)
        self.assertEqual(result,[])
        

if __name__ == '__main__':
    unittest.main()
   