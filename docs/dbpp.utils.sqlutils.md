<center>

**[dbpp.widgets](dbpp.widgets.md) package:** 
[GuiBaseClass](dbpp.widgets.guibaseclass.md) -
[AutoScrollbar](dbpp.widgets.autoscrollbar.md) -
[Balloon](dbpp.widgets.balloon.md) -
[Ctext](dbpp.widgets.ctext.md) -
[LabEntry](dbpp.widgets.labentry.md) -
[RoText](dbpp.widgets.rotext.md) -
[Scrolled](dbpp.widgets.scrolled.md) -
[SqlText](dbpp.widgets.sqltext.md) -
[StatusBar](dbpp.widgets.statusbar.md) -
[TableView](dbpp.widgets.tableview.md) -
[TextMixins](dbpp.widgets.textmixins.md) -
[XTableView](dbpp.widgets.xtableview.md) -
[XTreeView](dbpp.widgets.xtreeview.md) 

[dbpp.kroki](dbpp.kroki.md) - 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.krokiencoder.md) -
[dbpp.utils](dbpp.utils.md) - 
[dbpp.utils.SqlUtils](dbpp.utils.sqlutils.md)  -

**apps:** [dbpp.peditor](dbpp.peditor.pumleditor.md)


</center>

<!-- markdownlint-disable -->

<a href="../dbpp/utils/sqlutils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `utils.sqlutils`
dbpp.utils.SqlUtils - class to work with Sqlite3 and Csv files. 

This class provides methods to convert CSV and TAB files into Sqlite3 databases and as well allows the extraction of data from databases into CSV and TAB files  using Python as programming language. 

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



**Examples:**
 

```
     >>> import sys, os
     >>> sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
     >>> import dbpp.utils.sqlutils as sql
     >>> sqlo = sql.SqlUtils(':memory:')
     >>> sqlo.get_tables() 
     []
     >>> tabfile = os.path.join(os.path.dirname(__file__),"..","data","iris.tab")
     >>> tabfile
     '/home/groth/workspace/dbpp/dbpp/utils/../data/iris.tab'
     >>> sqlo.csv2sql(tabfile,"iris")
     150
     >>> sqlo.get_tables()
     ['iris']
     >>> sqlo.select("select RNames, Sepal_Length from iris limit 2")
     (['RNames', 'Sepal_Length'], [('R001', '5.1'), ('R002', '4.9')])
     
``` 


---

<a href="../dbpp/utils/sqlutils.py#L172"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `main`

```python
main(argv)
```

Runs the terminal application usually with sys.argv. 



**Arguments:**
 
 - <b>`argv`</b> (list):  arguments are in order: application. csvfile, sqlitefile, tablename  and optionally tabchar and quotechar 


---

<a href="../dbpp/utils/sqlutils.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>class</kbd> `SqlUtils`
Class to import and export data and to query information out of SQLite databases. 



**Attributes:**
 
 - <b>`self.filename (str)`</b>:  the name of the SQLite 3 database 
 - <b>`self.connection (sqlite3.Connection)`</b>:  the connection to the current database 



<a href="../dbpp/utils/sqlutils.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `__init__`

```python
__init__(filename=':memory:')
```

Initialize the object with a database filename or in memory. 



**Args:**
 
 - <b>`filename`</b> (str):  the filename of a SQLite 3 database, if it does not exists, it is silently created,  defaults to ':memory:'  






---

<a href="../dbpp/utils/sqlutils.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `csv2sql`

```python
csv2sql(csvfile, tablename, delimiter='\t', quotechar='"')
```

Import a CSV or TAB file as a new table into the data base. 



**Arguments:**
 
 - <b>`csvfile`</b> (str):  filename of a csvfile 
 - <b>`tablename`</b> (str):  name of the table to create in the current database 
 - <b>`delimiter`</b> (chr):  column delimiter, defaults to '    ' the tabstop 
 - <b>`quotechar`</b> (chr):  quoting character for strings with spaces, defaults to the double quote 



**Returns:**
 
 - <b>`int `</b>:  the number of rows added 

---

<a href="../dbpp/utils/sqlutils.py#L158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `get_columns`

```python
get_columns(tname)
```

Return the column names for the given table or view name. 

---

<a href="../dbpp/utils/sqlutils.py#L142"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `get_tables`

```python
get_tables()
```

Return the names of the tables of the database. 

---

<a href="../dbpp/utils/sqlutils.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `get_views`

```python
get_views()
```

Return the names of the views of the database. 

---

<a href="../dbpp/utils/sqlutils.py#L164"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `select`

```python
select(statement)
```

Return the result set for the given select statement. 

---

<a href="../dbpp/utils/sqlutils.py#L119"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>method</kbd> `sql2csv`

```python
sql2csv(tablename, csvfile)
```

Exporting a table from a SQLite3 database to a CSV file 



**Args:**
 
 - <b>`tablename`</b> (str):  name of the table to export 
 - <b>`csvfile`</b> (str):  name of the csv file for output  



**Returns:**
 
 - <b>`int `</b>:  number of data rows exported 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
