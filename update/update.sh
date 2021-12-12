#!/bin/bash
git reset --hard

git clean -default

git pull -f

./post_update.sh