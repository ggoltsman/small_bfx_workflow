
import os
import argparse
import modules
import unittest
import sqlite3


db_name='vcf.db'


class TestSQLQueries(unittest.TestCase):
    
    def test_select_pos(self):

        conn = sqlite3.connect(db_name)
        cur = conn.cursor()


        cur.execute("SELECT * FROM vcfTable WHERE POS = 17073043")
        res= cur.fetchall()
        self.assertEqual(res[0][1], 17073043, 'Position unit test failed.')        
        conn.close()

    def test_annot(self):
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        cur.execute("SELECT * FROM vcfTable WHERE POS = 17073043")
        res= cur.fetchall()
        self.assertTrue(res[0][-1].startswith('ANN='), 'Annotation unit test failed.')        
        conn.close()
        

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--vcf', help='vcf file', required=True)
    args = parser.parse_args()
    
    vcf_in = args.vcf
    vcf_annot = os.path.splitext(os.path.basename(vcf_in))[0] + '.ann.vcf'

    if not os.path.exists(vcf_annot):
        modules.runSnpEff(vcf_in, vcf_annot)
    if not os.path.exists(db_name):
        modules.loadIt(db_name, vcf_annot)
    
    
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
