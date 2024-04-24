#!/bin/bash
  
cd ${result_folder}

mkdir outputs

for year in $(seq $param_start_year $param_end_year); do

mv $year outputs/

done

zip -r outputs.zip outputs/

rm -rf outputs/

rm -rf temp/
