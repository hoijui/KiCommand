import unittest
from kicommand import run as kc

class TestDrawing(unittest.TestCase):

    def test_showparam_drawparams(self):
        self.assertEqual(kc('showparam'),{'h': 1000000.0, 'zp': 0, 'zt': 0, 't': 500000.0, 'w': 1000000.0, 'l': 'F.Cu'} )
        self.assertEqual(kc('4,2,3 mm B.Cu drawparams showparam'),{'h': 3000000.0, 'zp': 0, 'zt': 0, 't': 4000000.0, 'w': 2000000.0, 'l': 'B.Cu'} )
        
    def test_drawpoly(self):
        track = kc('clear 0.5 mm t param F.Cu l param 10,10,20,30 mm '
                        'drawpoly delist delist')

    def test_drawsegments(self):
        result = kc('clear 0,0,1,1 mm drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0]),1)
        # Test single list of list of numbers:
        result = kc('delist remove',returnval=-1)
        self.assertEqual(result,[])
        
        result = kc('clear 0,0,1,1 mm list drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0][0]),1)
        result = kc('delist remove',returnval=-1)
        self.assertEqual(result,[])
        
        # Test single list of numbers:
        result = kc('clear 0,0,1,1,2,2,3,3 mm list drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0][0]),3)
        result = kc('delist remove',returnval=-1)
        self.assertEqual(result,[])
        
        # Test two lists of numbers:
        result = kc('clear 0,0,1,1 mm list 2,2,3,3 mm list concat drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0][0]),1)
        self.assertEqual(len(result[0][1]),1)
        result = kc('copy 1 index remove 0 index remove',returnval=-1)
        self.assertEqual(result,[])
        
        result = kc('clear 0,0,1000000,1000000 ,2000000,2000000,3000000,3000000 concat drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0][0]),3)
        result = kc('delist remove',returnval=-1)
        self.assertEqual(result,[])
        
        result = kc('clear 0,0,1000000,1000000,2000000,2000000,3000000,3000000 drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0][0]),3)
        result = kc('delist remove',returnval=-1)
        self.assertEqual(result,[])
        
        result = kc('clear 0,0,1000000,1000000 list 2000000,2000000,3000000,3000000 list concat drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0][0]),1)
        self.assertEqual(len(result[0][1]),1)
        result = kc('copy 1 index remove 0 index remove',returnval=-1)
        self.assertEqual(result,[])
        
        result = kc('clear 0,0 mm wxpoint 1,1 mm wxpoint concat 2,2 mm wxpoint concat 3,3 mm wxpoint concat drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0][0]),3)
        result = kc('delist remove',returnval=-1)
        self.assertEqual(result,[])
        
        result = kc('clear 0,0 mm wxpoint 1,1 mm wxpoint concat list 2,2 mm wxpoint 3,3 mm wxpoint concat list concat drawpoly',returnval=-1)
        self.assertEqual(len(result),1)
        self.assertEqual(len(result[0][0]),1)
        self.assertEqual(len(result[0][1]),1)
        result = kc('copy 1 index remove 0 index remove',returnval=-1)
        self.assertEqual(result,[])
        
   
if __name__ == '__main__':
    unittest.main()
   