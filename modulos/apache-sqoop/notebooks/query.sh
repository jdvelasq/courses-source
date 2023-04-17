sqoop eval \
    --connect jdbc:mysql://localhost:3306/demo_db \
    --username sqoop \
    --password secret \
    --query "SELECT * FROM drivers LIMIT 3"
