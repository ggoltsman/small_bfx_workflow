#!/usr/bin/env bash
#set -e

python ./workflow.py -v data/test.chr22.vcf -o validation
ret=$?
if [ $ret -ne 0 ]; then
    echo "Validation run DID NOT COMPLETE"
    echo $retMe
    exit 1
else
    echo "validation run completed"
fi

pytest test_results.py
echo "unit tests completed"



