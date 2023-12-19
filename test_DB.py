
import os
import sqlite3
print(f"SQLite3 {sqlite3.sqlite_version}")
import genomicsqlite
print(f"GenomicSQLite {genomicsqlite.__version__}")


dbconn = sqlite3.connect('data/TxDb.Hsapiens.UCSC.hg38.knownGene.sqlite', uri=True)

# use the Genomics extension to create a compressed version of the database

dbconn.executescript(genomicsqlite.vacuum_into_sql(dbconn, "data/hg38kg.genomicsqlite"))

dbconn.close()
