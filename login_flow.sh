#!/bin/bash
echo "enter email address:"
read email
echo "please enter your password:"
read -s password

token=$(curl -X POST http://localhost:3333/auth/token/login/ --data "email=$email&password=$password"|jq .auth_token |sed 's/\"//g')
curl -LX GET http://localhost:3333/auth/users/me/ -H "Authorization: Token $token"
curl -X POST http://localhost:3333/auth/token/logout/ -H "Authorization: Token $token"
