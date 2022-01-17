#!/bin/bash

#start up docker
systemctl enable docker --now

#configure registry
> /etc/docker/daemon.json
file=/etc/docker/daemon.json
echo { > ${file}
sed -i '$a\\t"exec-opts":["native.cgroupdriver=systemd"],' ${file}
sed -i '$a\\t"registry-mirrors":["https://hub-mirror.c.163.com"],' ${file}
sed -i  '$a\\t"insecure-registries":["192.168.1.100:5000","registry:5000"]' ${file}
echo } >> ${file}

#load images to localhost

Exists=`docker images | awk "NR==2{print}"`
if [ -z ${Exists} ];then
for images in ~/base-images/*.tar.gz
do
docker load -i ${images}
done 
fi

#upload images to registry
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
