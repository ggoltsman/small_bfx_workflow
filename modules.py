import os
import pandas
import sqlite3
import subprocess


def loadIt(db_name, vcf_fn):
    print(f"SQLite3 {sqlite3.sqlite_version}")
    conn = sqlite3.connect(db_name)

    header_cnt = 0
    with open(vcf_fn) as fp:
        for line in fp:
            if line.startswith("##"):
                header_cnt += 1
            if line.startswith("#CHROM"):
                break

    df = pandas.read_csv(vcf_fn, sep="\t", skiprows=header_cnt)
    df.to_sql("vcfTable", conn, index=False)
    conn.commit()
    conn.close()


def runSnpEff(vcf_in, vcf_out, ref_name="GRCh37.75"):
    os.system("java -version")
    snpEff_jar = (
        "/usr/local/Caskroom/miniconda/base/envs/BFX//share/snpeff-5.2-0/snpEff.jar"
    )
    assert os.path.exists(snpEff_jar)
    cmd = f"java -Xmx8g -jar {snpEff_jar} {ref_name} {vcf_in} > {vcf_out}"

    print("Running ", cmd)

    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command {cmd} failed with error {e.returncode}")
