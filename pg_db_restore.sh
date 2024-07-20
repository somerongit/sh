#!/bin/bash

DB_USER="change_me_user"
RESTORE_DB_NAME="change_me_user"
CONTAINER_NAME="postgres_restore"
BACKUP_FILE="./backup.gz"
gunzip $BACKUP_FILE
docker exec -i $CONTAINER_NAME psql -U $DB_USER $RESTORE_DB_NAME < ./backup
echo "Database restored from $BACKUP_FILE"

#  Backup 
#  docker exec -t $DB_CONTAINER_NAME pg_dump -U $DB_USER $DB_BACKUP_NAME | gzip > /home/user/app/backup/app_db_dump_`date +%d-%m-%Y_%H-%M-%S`.gz
