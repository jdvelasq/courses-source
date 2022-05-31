
sqoop import \
    --connect jdbc:mysql://localhost:3306/demo_db \
    --username sqoop \
    --password secret \
    --table drivers \
    --hive-import \
    --m 1
