import os
import sqlite3
import subprocess
import time
import pandas


def loadIt(vcf_fn, db_name):
    assert os.path.exists(vcf_fn)

    table = "vcfTable"
    if os.path.exists(db_name):
        print(
            f'Warning: pre-exsiting database {db_name} found. Will create table "{table}" or APPEND to it, if exists.. '
        )
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
    df.to_sql(
        table, conn, index=False, if_exists="append"
    )  # appends to an existing table! Will not check for duplicates

    cursor = conn.cursor()
    query = "select * from " + table
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"DB table {table} now contains  {len(results)} entries")

    conn.commit()
    conn.close()

    return len(results)


def runSnpEff(vcf_in, vcf_out, ref_name="GRCh37.75"):
    assert os.path.exists(vcf_in)

    if os.path.exists(vcf_out):
        pause = 5
        print(
            f"Warning: pre-existing annotated vcf file {vcf_out} found. Will OVERWRITE this file in {pause} seconds..!"
        )
        time.sleep(pause)

    os.system("java -version")
    # cmd = f"snpEff {ref_name} {vcf_in} > {vcf_out}"  #Running like this may use up all the memory on the system

    # to avoid memory heap overruns, we call java explicitly on the .jar file. But we first need to find it
    # E.g.,   "/usr/local/Caskroom/miniconda/base/envs/BFX//share/snpeff-5.2-0/snpEff.jar"

    if os.path.exists("./snpEff"):
        snpEff_jar = "./snpEff/snpEff.jar"
        assert os.path.exists(snpEff_jar)
    else:  # assume snpEff is installed somewhere and is in my $PATH
        find_jar_cmd = "find $(dirname $(which snpEff))/.. -name snpEff.jar"
        snpEff_jar = (
            subprocess.run(
                find_jar_cmd, shell=True, check=False, stdout=subprocess.PIPE
            )
            .stdout.decode("utf-8")
            .split()[0]
        )
        assert os.path.exists(snpEff_jar)

    cmd = f"java -Xmx8g -jar {snpEff_jar} {ref_name} {vcf_in} > {vcf_out}"

    print("Running ", cmd)

    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command {cmd} failed with error {e.returncode}")
