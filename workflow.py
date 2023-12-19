
import os
import argparse
import modules
import sqlite3



if __name__ == '__main__':

    db_name='vcf.db'
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-v','--vcf', help='vcf file', required=True)
    args = parser.parse_args()
    
    vcf_in = args.vcf
    vcf_annot = os.path.splitext(os.path.basename(vcf_in))[0] + '.ann.vcf'

    if not os.path.exists(vcf_annot):
        modules.runSnpEff(vcf_in, vcf_annot)
    if not os.path.exists(db_name):
        modules.loadIt(db_name, vcf_annot)
    
