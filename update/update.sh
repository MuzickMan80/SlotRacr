#!/bin/bash
git reset --hard

git clean -fxd

git pull -f

./update/post_update.sh