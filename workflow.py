import os
import argparse
import modules


if __name__ == "__main__":
    db_name = "vcf.db"

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--vcf", help="vcf file", required=True)
    parser.add_argument(
        "-o",
        "--out_pref",
        help="output prefix (defaut: same as input vcf)",
        required=False,
    )
    parser.add_argument(
        "-b",
        "--bootstrap",
        help="bootstrap from existing annotated vcf (bypasses snpEff)",
        action="store_true",
        required=False,
    )
    args = parser.parse_args()

    vcf_in = args.vcf
    if not os.path.exists(vcf_in):
        raise SystemExit("Input vcf file does not exist")

    if args.out_pref:
        vcf_annot = args.out_pref + ".ann.vcf"
    else:
        vcf_annot = os.path.splitext(os.path.basename(vcf_in))[0] + ".ann.vcf"

    if args.bootstrap:
        assert os.path.exists(vcf_annot)
    else:
        modules.runSnpEff(vcf_in, vcf_annot)

    modules.loadIt(vcf_annot, db_name)
