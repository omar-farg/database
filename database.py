import sqlite3
db=sqlite3.connect("app.db")
cr=db.cursor()
#t=('java' ,'65' ,2)
#cr.execute("insert into skills values (?,?,?)",t)
cr.execute("select * from skills order by id asc limit 2")
def cs():
    db.commit()
    db.close()
    print("closed")
id=input("id: ")
mess="""
what do you want?
"s" show skills
"a" add new
"d" delete
"u" update
"q" quit
"""
user=input(mess).strip().lower()
comm=["s","a","d","u","q"]
def show():
    cr.execute(f"select * from skills where id={id}")
    result=cr.fetchall()
    print(f"{len(result)}")
    for row in  result:
        print(f"{row[0]} {row[1]}%")   
    cs()
def add():
    sk=input("skill name:").strip().capitalize()
    cr.execute(f"select name from skills where name='{sk}' and id='{id}'")
    result=cr.fetchone()
    if result ==None:
        print("you can add")
        prog=input("skill progress:").strip()
        cr.execute(f"insert into skills(name ,progress ,id) values('{sk}' ,'{prog}' ,'{id}')")
    else:
        print("you can add it")
    
    cs()
def delete():
    sk=input("skill name:").strip().capitalize()
    cr.execute(f"delete from skills where name ='{sk}' and id='{id}' ")
    cs()
def update():
    sk=input("skill name:").strip().capitalize()
    prog=input("skill progress:").strip()
    cr.execute(f"update skills set progress = '{prog}' where name ='{sk}' and id='{id}'")
    cs()
def quit():
    cs()

if user in comm:
    print(f"command found {user}")
    if user == "s":
        show()
    elif user == "d":
        delete()
    elif user == "u":
        update()
    elif user == "a":
        add()
    else:
        print("app closed")
else:
    print(f"\"{user}\" not found")
