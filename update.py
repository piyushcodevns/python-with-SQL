from sqlalchemy import create_engine, text
engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/piyush")
with engine.connect() as conn:
    conn.execute(
        text("update school set name='Rahul' where id=4")
    )
    conn.commit()
print("Update done")
