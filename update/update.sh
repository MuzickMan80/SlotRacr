#!/bin/bash

# NOTE: changes to this file will require two ureboots to take effect
git reset --hard

git clean -fxd

git pull -f

./update/post_update.sh