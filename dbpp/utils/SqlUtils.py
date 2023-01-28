#!/usr/bin/env python3
"""
dbpp.utils.SqlUtils - class to work with Sqlite3 and Csv files.

This class provides methods to convert CSV and TAB files into Sqlite3 databases
and as well allows the extraction of data from databases into CSV and TAB files 
using Python as programming language.

The class has the following attributes and methods:

```{.kroki echo=false dia=plantuml cache=false}
@startuml
class SqlUtils {
    + self.filename
    + __init__(filename)
    + csv2sql(filename)
    + getTables()
    + getViews()
    + getColumns()
}
@enduml
```

Examples:

```
    >>> import sys, os
    >>> sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
    >>> import dbpp.utils.SqlUtils as sql
    >>> sqlo = sql.SqlUtils(':memory:')
    >>> sqlo.getTables() 
    []
    >>> tabfile = os.path.join(os.path.dirname(__file__),"..","data","iris.tab")
    >>> tabfile
    '/home/groth/workspace/dbpp/dbpp/utils/../data/iris.tab'
    >>> sqlo.csv2sql(tabfile,"iris")
    150
    >>> sqlo.getTables()
    ['iris']
    >>> sqlo.select("select RNames, Sepal_Length from iris limit 2")
    (['RNames', 'Sepal_Length'], [('R001', '5.1'), ('R002', '4.9')])
    
```
"""

import csv
import sqlite3
import re, sys

class SqlUtils():
    """Class to import and export data and to query information out of SQLite databases.
    
    Attributes:
        self.filename (str): the name of the SQLite 3 database
        self.connection (sqlite3.Connection): the connection to the current database
        
    """ 
    def __init__(self,filename=':memory:'):
        """Initialize the object with a database filename or in memory.
        
        Args:
            filename (str): the filename of a SQLite 3 database, if it does not exists, it is silently created,  defaults to ':memory:'
                            
        """
        self.filename= filename
        # Create the connection to the database
        self.connection = sqlite3.connect(self.filename)
    def __del__ (self):
        self.connection.commit()
        self.connection.close()
        
    def csv2sql(self,csvfile,tablename,delimiter='\t',quotechar='"'):
        """Import a CSV or TAB file as a new table into the data base.
        
        Arguments:
            csvfile (str): filename of a csvfile
            tablename (str): name of the table to create in the current database
            delimiter (chr): column delimiter, defaults to '\t' the tabstop
            quotechar (chr): quoting character for strings with spaces, defaults to the double quote
            
        Returns:
            int : the number of rows added
        """
        # Create the table
        cursor = self.connection.cursor()

        cursor.execute('DROP TABLE IF EXISTS '+tablename)
        self.connection.commit()
        # Load the CSV file into CSV reader
        csvfile = open(csvfile, 'r')
        creader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
        x=1
        for row in creader:
            if x == 1:
                ncol=len(row)
                stm="CREATE TABLE "+tablename+" ("
                istm="INSERT INTO "+tablename+" VALUES"+" ("
                for col in row:
                    stm=stm+col.replace(".","_")+" TEXT"
                    istm=istm+"?"
                    if col != row[len(row)-1]:
                        stm = stm+","
                        istm = istm+","
                stm=stm+")"
                istm=istm+")"
                x=x+1
                #print(stm)
                cursor.execute(stm)
            else:
                x = x + 1
                if (len(row)>0):
                    if (ncol+1) == len(row):
                        # R data.frame with row names
                        cursor.execute(istm,row[1:len(row)])
                    else:
                        cursor.execute(istm,row)
        return(x-2)
        
    def sql2csv(self, tablename, csvfile):
        """Exporting a table from a SQLite3 database to a CSV file
        
        Args:
            tablename (str): name of the table to export
            csvfile (str): name of the csv file for output 
            
        Returns:
            int : number of data rows exported
        """
        cursor = connection.cursor()
        with open(csvfile, "w") as f:
            writer = csv.writer(f)
            cursor.execute(f"SELECT * FROM {tablename}")
            rows = cursor.fetchall()
            writer.writerow([i[0] for i in cursor.description])
            for row in rows:
                writer.writerow(row)
                
        connection.close()
        return(len(rows))
        
    #    pass
    def getTables (self):
        """Return the names of the tables of the database."""
        curs=self.connection.cursor()
        res=[]
        curs.execute("select name from sqlite_master where type = 'table'")
        for row in curs:
            res.append(row[0])
        return(res)                
    def getViews (self):
        """Return the names of the views of the database."""
        curs=self.connection.cursor()
        res=[]
        curs.execute("select name from sqlite_master where type = 'view'")
        for row in curs:
            res.append(row[0])
        return(res)                
    def getColumns(self,tname):
        """Return the column names for the given table or view name."""
        curs=self.connection.cursor()
        curs.execute('PRAGMA TABLE_INFO({})'.format(tname))
        names = [tup[1] for tup in curs.fetchall()]
        return(names)
    def select(self,statement):
        """Return the result set for the given select statement."""
        curs = self.connection.cursor()
        curs.execute(statement)
        names = list(map(lambda x: x[0], curs.description))
        res=curs.fetchall()
        return names,res

def main(argv):
    """Runs the terminal application usually with sys.argv.
    
    Arguments:
        argv (list): arguments are in order: application. csvfile, sqlitefile, tablename
            and optionally tabchar and quotechar
    """
    tabchar='\t'
    quotechar='"'
    if len(argv) < 4:
        print("Usage: csvfile sqlitefile tablename ?tabchar quotechar?")
        sys.exit(0)
    if len(argv) == 6:
        quotechar = argv[5]
        tabchar= argv[4]
    if len(argv) == 5:
        tabchar =argv[4]
    sq=SqlUtils(argv[2])
    sq.csv2sql(argv[1],argv[3],tabchar,quotechar)

if __name__ == "__main__":
    #print(sys.argv)
    main(sys.argv)
