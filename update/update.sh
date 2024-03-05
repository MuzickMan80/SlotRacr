#!/bin/bash

# NOTE: changes to this file will require two reboots to take effect
git reset --hard

git clean -fxd

timeout 30s bash -c 'until git pull &> /dev/null; do sleep 1; done'

./update/post_update.sh