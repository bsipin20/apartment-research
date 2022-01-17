#!/bin/sh

until curl questdb:9000
do
  sleep 5
done

python3 -m crawl.sources.craigs_list 
