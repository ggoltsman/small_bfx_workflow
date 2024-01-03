#!/usr/bin/env bash
#set -e
. "/usr/local/Caskroom/miniconda/base/etc/profile.d/conda.sh"

conda activate BFX
python ./workflow.py -v data/test.chr22.vcf -o validation
ret=$?
if [ $ret -ne 0 ]; then
    echo "Validation run DID NOT COMPLETE"
    echo $retMe
    exit 1
else
    echo "validation run completed"
fi

conda activate py3
pytest && echo "unit tests completed"


