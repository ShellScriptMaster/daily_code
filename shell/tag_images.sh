#!/bin/bash
REPO_PORT='192.168.4.100:5000'
docker images | awk 'NR>1{print$1}'  >> ORIGIN_IMG.txt
docker images | awk 'NR>1{print$2}'  >> ORIGIN_TAG.txt
awk -F/ '{print $2}'   ORIGIN_IMG.txt >> IMG_NAME.txt
LINES=`sed -n '$=' ORIGIN_IMG.txt`
for num in `seq 1 $LINES ` 
do
ORIGIN_IMG=`sed  -n  "${num}p"  ORIGIN_IMG.txt`
ORIGIN_TAG=`sed  -n  "${num}p"  ORIGIN_TAG.txt`
IMG_NAME=`awk -F/ '{print $2}' ORIGIN_IMG.txt | sed -n "${num}p"`
docker tag   $ORIGIN_IMG:$ORIGIN_TAG  $REPO_PORT/$IMG_NAME:$ORIGIN_TAG
docker push  $REPO_PORT/$IMG_NAME:$ORIGIN_TAG
#docker rmi  $REPO_PORT/$IMG_NAME:$ORIGIN_TAG
#echo  "  $ORIGIN_IMG:$ORIGIN_TAG  $REPO_PORT/$IMG_NAME:$ORIGIN_TAG"

done

rm -rf ORIGIN_IMG.txt ORIGIN_TAG.txt IMG_NAME.txt
