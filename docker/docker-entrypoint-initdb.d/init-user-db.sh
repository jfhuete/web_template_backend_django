#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER $POSTGRES_NOVA_USER with encrypted password '$POSTGRES_NOVA_PASSWORD';
	CREATE DATABASE $POSTGRES_NOVA_DB;
	GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_NOVA_DB TO $POSTGRES_NOVA_USER;
EOSQL