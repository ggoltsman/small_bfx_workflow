# small_bfx_workflow

The workflow run snpEff on a bare-bomes vcf file and produces an annotated vcf which is then entered into an sqlite3 database

1. set up the environment
. "/usr/local/Caskroom/miniconda/base/etc/profile.d/conda.sh"
conda activate BFX

2. execute the workflow
python ./workflow.py -v [vcf file]
