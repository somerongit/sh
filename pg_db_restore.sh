#!/bin/bash

DB_USER="change_me_user"
RESTORE_DB_NAME="change_me_user"
CONTAINER_NAME="postgres_restore"
BACKUP_FILE="./backup.gz"
gunzip $BACKUP_FILE
docker exec -i $CONTAINER_NAME psql -U $DB_USER $RESTORE_DB_NAME < ./backup
echo "Database restored from $BACKUP_FILE"
