#!/usr/bin/env zsh
#Simple script to deploy to AWS Lambda and API Gateway
#
# To undeploy: zappa undploy dev
# To redeploy: zappa update dev
#
# Zappa repo: https://github.com/Miserlou/Zappa
#

export VIRTUAL_ENVS=$HOME/.virtualenvs

source $VIRTUAL_ENVS/`pwd | sed 's#.*/##'`/.env/bin/activate

zappa undeploy dev


echo ""
echo " Zappa repo: https://github.com/Miserlou/Zappa"
