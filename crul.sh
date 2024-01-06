# !/bin/bash


for ((i=101; i<=200; i++))
  do
    url="https://www.purplle.com/neo/merch/listing?list_type=category&list_type_value=men&page=$i&sort_by=rel&elite=0&custom=&mode_device=desktop&ab_experiment_listing=e"\
    response=$(curl "$url" \
      | jq '.' >> data.txt 
      
  )
  done 

