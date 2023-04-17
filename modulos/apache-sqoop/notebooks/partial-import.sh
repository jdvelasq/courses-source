
hdfs dfs -rm -r /tmp/drivers

sqoop import \
    --connect jdbc:mysql://localhost:3306/demo_db \
    --username sqoop \
    --password secret \
    --table drivers \
    --target-dir /tmp/drivers/ \
    -m 1 \
    --where "driverId=10"
