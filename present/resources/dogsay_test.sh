#!/usr/bin/env bash
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
sleep 3 &
DOGSAY_WAIT_PID=$! ${SCRIPT_DIR}/dogsay.sh animate 'waiting...'
${SCRIPT_DIR}/dogsay.sh talk 'done!'
