# DBMS final project
```
Name: 許郁翎
ID: F74072277
系級: 資訊111
```
## system architecture and environment
### device
```
裝置名稱	LAPTOP-045SKT5O
處理器	Intel(R) Core(TM) i5-10210U CPU @ 1.60GHz   2.11 GHz
已安裝記憶體(RAM)	8.00 GB (7.87 GB 可用)
系統類型	64 位元作業系統，x64 型處理器
```
### packages
```
GUI: Tkinter (python)
database: SQlite3
```
## screenshot of interface and description

```
this is a still developing program!!
the part that will be use to demo is the query part, the APP and release options in the button part
```

### file description
```
main.py
the main program

button.py
the code of the interface to do button demo

query.py
the code of the interface to do query demo

db.py
the code to create a new empty table

tmp.py
plz ignore it...

info.txt
the file record the data inserted into database.db, and the demo instructions
```

### screenshots and description

```
the main page
```
![](https://i.imgur.com/1CBxqsx.png)
```
the query page
```
![](https://i.imgur.com/vOwtrOS.png)
```
the button page
```
![](https://i.imgur.com/Uze2HAj.png)
```
for the instruction as follows:
SELECT-FROM-WHERE, DELETE, INSERT, UPDATE, COUNT, SUM, MAX, MIN, AVG, HAVING 

plz choose the option APP
```
![](https://i.imgur.com/TNvAZq5.png)
```
for the instruction as follows:
IN, NOT IN, EXISTS, NOT EXISTS

plz choose the option release
```
![](https://i.imgur.com/hm6s63T.png)

## database design

### ER diagram
![](https://i.imgur.com/rl4t3P4.png)
The picture above is my ER diagram, the blue rectangle are `entities`, and the red diamond are `relationships`.  

The yellow oval are `attributes`, and the orange ones are `key attributes`.  
The green ones are `attributes of relationships`.  



### Relation Schema
![](https://i.imgur.com/saz7iug.png)

### table, attribute and relationship

The figure above shows relation schema in my database system. Similar with my ER diagram, the yellow part are attributes of `entities`, and the ones with red words are `key attributes`, so called `primary keys`. The green ones are `attributes of relationships`.  

The red ones are `foreign keys`. `work_for_id`, which means the the ID of the company that developer work for, matchs `company_id` in the table, `company`. `release_id`, which represents the ID of the company that releases the APP, also matches `company_id`.





## reference tutorial
[Python GUI's With TKinter](https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=1&ab_channel=Codemy.com)  
[SQLite Tutorial](https://www.sqlitetutorial.net/)  

## additional link
[project demo youtube link](https://www.youtube.com/watch?v=F1o3P8PhlhY)  
[final project GitHub](https://github.com/tsaoni/2022Spring-DBMS)
