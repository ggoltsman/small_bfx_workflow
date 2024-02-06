The workflow runs snpEff on a bare-bomes vcf file and produces an annotated vcf which is then entered into an sqlite3 database


INSTALLL:

make install


TEST:

make test lint format


RUN THE VALIDATION WORKFLOW:

./run_test_workflow.sh


RUN TNE WORKFLOW WITH YOUR DATA:

python ./workflow.py -v [vcf file]
