import pymysql

#MySQL config insert
config={

        'host':'',
        'port':3306,
        'user':'',
        'passwd':'',
        'db':'try',
        'charset':'',
        'local_infile':1

    }
conn=pymysql.connect(** config)
cur=conn.cursor()
print('success')
userid=123
sql_cmd="select * from user where uid='"+str(userid)+"'"
sql_cmd
query_data=db.engine.excute(sql_cmd)
if len(list(query_data))==0:
    sql_cmd="insert into user (uid) values('"+str(userid)+"');"
    db.engine.excute(sql_cmd)
