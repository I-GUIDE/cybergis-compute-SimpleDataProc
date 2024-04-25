#!/bin/bash

#zip up outputs
  
cd ${result_folder}

zip -r outputs.zip outputs/

#clean up other files
for year in $(seq $param_start_year $param_end_year); do

rm -rf $year

done

rm -rf outputs/

rm -rf temp/
