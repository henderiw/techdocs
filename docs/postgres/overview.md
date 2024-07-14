# postgres

## Introduction

### RDBMS

Relation Database Management system (POSTGRESSQL, MYSQL, MariaDB, MicroSoft SQL)

- tables
- columns (primary key, foreign key)
- row

Instance: memory, process
DataBase: disk (data, logs (transactions for playback), config parameters)

### POSTGRESQL

30+ years development -> open source

An elephant never forgets

- user initiates 
- shared memory (buffers, in memory cached) (shared buffers, WAL buffers) -> logs transaction
- physical files (data files, WAL files, archive files, log files)
- utility processes (Writer, WAL Writer, CheckPointer, Archiver, Logging, Stats, Autovaccuum)

WAL: Write Ahead Log
MultiVersion ConcurrencyControl: concurrency through snapshotting, lots of garbage collection 

### Clustering (General concept)

Replication: (default option)
- Master with Hot/Multiple Warm Standby
- Write: Master -> Hot Standby
- Read: Hot Standby
- Synchronous: immediate failover -> ack the transaction

Multi-Master: (loadbalancing)
- Shared VIP with multiple masters
- All able to handle read and write

### Client

GUI
- pgAdmin
- DBaever
- Azure Data Studio
CLI:
- PSQL
- phpPgAdmin

```
sudo su - postgres
-> peer authentication

psql
postgres=#\q -> exit

psql -d acweb

psql -h 172.31.22.24 -U postgres -W -p 1433

# execute a file
psql -d acweb -f test.sql
```

```
\?
\dt
\dn -> schemas
\di sales.* -> indexes
\dv sales.* -> views
\dy sales.* -> triggers
\du users
\dg groups/roles

\s -> show history
\g -> reexecute last command
\set -> list of vars
\set QUIET 'on'
\timing -> shows executin time
\x -> shows extended view
```

