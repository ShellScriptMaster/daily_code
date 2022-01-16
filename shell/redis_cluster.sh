#!/bin/bash
#shutdown the redis
/etc/init.d/redis_6379 stop 
CONF=/etc/redis/6379.conf
INIT=/etc/init.d/redis_6379
#modify the redis config file /etc/redis/6379.conf
IP=`ifconfig eth0  | sed -n '2p' | awk '{print $2}'`
HOSTNAME=`ifconfig eth0  | sed -n '2p' | awk '{print $2}'| awk -F\.  '{print $NF}'`
sed -i  "/^bind /s/127.0.0.1/${IP}/ " $CONF  #bind-modify
sed -i "/^port/s/6379/88${HOSTNAME}/" $CONF   #port-modify
sed -i '/^# cluster-enabled/s/#//' $CONF   # enabled-cluster
sed -i  '/cluster-node-timeout/s/#//' $CONF  #enabled  setting timeout 
sed -i  '/cluster-node-timeout/s/15000/5000/' $CONF  #setting timeout 5000
sed -i '/cluster-config-file/s/#//' $CONF #point out the  cluster-config-file
#modify the startup-script /etc/init.d/redis_6379
sed -i "/REDISPORT=/s/6379/88${IP}/"  $INIT
sed -i  "2aHOSTNAME=$IP"  $INIT
sed -i '/$CLIEXEC -p $REDISPORT shutdown/c/$CLIEXEC -p $REDISPORT -h $HOSTNAME shutdown/'  $INIT
#start up redis
/etc/init.d/redis_6379 start 
