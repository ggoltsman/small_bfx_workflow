#!/usr/bin/env bash
set -e

. "/usr/local/Caskroom/miniconda/base/etc/profile.d/conda.sh"
conda activate BFX
python ./workflow.py -v data/test.chr22.vcf
echo "validation run completed"

conda activate py3
pytest
echo "unit tests completed"
