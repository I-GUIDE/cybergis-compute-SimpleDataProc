#!/bin/bash
  
mkdir /compute_shared/${job_id}

cd ${result_folder}

for year in $(seq $param_start_year $param_end_year); do

mv $year /compute_shared/${job_id}/

done

cd /compute_shared/${job_id}/

zip -r output.zip *
