<center>

**[dbpp.widgets](dbpp.widgets.md) package:** 
[GuiBaseClass](dbpp.widgets.GuiBaseClass.md) -
[AutoScrollbar](dbpp.widgets.AutoScrollbar.md) -
[Balloon](dbpp.widgets.Balloon.md) -
[Ctext](dbpp.widgets.Ctext.md) -
[LabEntry](dbpp.widgets.LabEntry.md) -
[RoText](dbpp.widgets.RoText.md) -
[Scrolled](dbpp.widgets.Scrolled.md) -
[SqlText](dbpp.widgets.SqlText.md) -
[StatusBar](dbpp.widgets.StatusBar.md) -
[TableView](dbpp.widgets.TableView.md) -
[TextMixins](dbpp.widgets.TextMixins.md) -
[XTableView](dbpp.widgets.XTableView.md) -
[XTreeView](dbpp.widgets.XTreeView.md) 

[dbpp.kroki](dbpp.kroki.md) - 
[dbpp.kroki.KrokiEncoder](dbpp.kroki.KrokiEncoder.md) -
[dbpp.utils](dbpp.utils.md) - 
[dbpp.utils.SqlUtils](dbpp.utils.SqlUtils.md)  -

**apps:** [dbpp.peditor](dbpp.peditor.PumlEditor.md)


</center>

<!-- markdownlint-disable -->

<a href="../dbpp/utils/SqlUtils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

# <kbd>module</kbd> `SqlUtils.py`
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


---

<a href="../dbpp/utils/SqlUtils.py#L149"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

## <kbd>function</kbd> `main`

```python
main(argv)
```

Runs the terminal application usually with sys.argv. 



**Arguments:**
 
 - <b>`argv`</b> (list):  arguments are in order: application. csvfile, sqlitefile, tablename  and optionally tabchar and quotechar 


---

## <kbd>class</kbd> `SqlUtils`
Class to import and export data and to query information out of SQLite databases. 



**Attributes:**
 
 - <b>`self.filename (str)`</b>:  the name of the SQLite 3 database 
 - <b>`self.connection (sqlite3.Connection)`</b>:  the connection to the current database 



<a href="../dbpp/utils/SqlUtils.py#L58"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `__init__`

```python
__init__(filename=':memory:')
```

Initialize the object with a database filename or in memory. 



**Args:**
 
 - <b>`filename`</b> (str):  the filename of a SQLite 3 database, if it does not exists, it is silently created,  defaults to ':memory:'  






---

<a href="../dbpp/utils/SqlUtils.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `csv2sql`

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

<a href="../dbpp/utils/SqlUtils.py#L135"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `getColumns`

```python
getColumns(tname)
```

Return the column names for the given table or view name. 

---

<a href="../dbpp/utils/SqlUtils.py#L119"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `getTables`

```python
getTables()
```

Return the names of the tables of the database. 

---

<a href="../dbpp/utils/SqlUtils.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `getViews`

```python
getViews()
```

Return the names of the views of the database. 

---

<a href="../dbpp/utils/SqlUtils.py#L141"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square" /></a>

### <kbd>function</kbd> `select`

```python
select(statement)
```

Return the result set for the given select statement. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
