import os
import argparse
import modules


if __name__ == "__main__":
    db_name = "var.db"

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", help="vcf file", required=True)
    parser.add_argument("-o", "--out_pref", help="output prefix (defaut: same as input vcf)", required=False)    
    args = parser.parse_args()

    vcf_in = args.vcf
    
    if args.out_pref:
        vcf_annot = args.out_pref + ".ann.vcf"
    else:
        vcf_annot = os.path.splitext(os.path.basename(vcf_in))[0] + ".ann.vcf"

    modules.runSnpEff(vcf_in, vcf_annot)
    
    modules.loadIt(vcf_annot, db_name)
