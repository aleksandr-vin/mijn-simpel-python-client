#!/usr/bin/env bash

curl 'https://mijn.simpel.nl/api/login' \
-X 'POST' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Content-Type: application/json;charset=utf-8' \
-H 'Origin: https://mijn.simpel.nl' \
-H 'Accept-Language: en-us' \
-H 'Host: mijn.simpel.nl' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15' \
     -H 'Referer: https://mijn.simpel.nl/login' \
     --cookie-jar cookies \
     -v \
--data-binary "{\"username\":\"${MIJN_SIMPEL_USERNAME}\",\"password\":\"${MIJN_SIMPEL_PASSWORD}\",\"remember\":null}"


curl 'https://mijn.simpel.nl/api/account/subscription-overview' \
-X 'GET' \
-H 'Accept: application/json, text/plain, */*' \
-H 'Host: mijn.simpel.nl' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15' \
-H 'Accept-Language: en-us' \
     -H 'Referer: https://mijn.simpel.nl/overzicht-abonnementen?previous_route=selfcare/dashboard' \
     --cookie cookies \
     -v

curl 'https://mijn.simpel.nl/api/dashboard?sid=s255560638' \
-X 'GET' \
-H 'Host: mijn.simpel.nl' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15' \
-H 'Accept-Language: en-us' \
-H 'Referer: https://mijn.simpel.nl/?sid=s255560638' \
     --cookie cookies \
     -v

