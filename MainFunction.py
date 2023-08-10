
def appender(Records):
    import sqlite3
    con = sqlite3.connect('receipt.db')
    cursor = con.cursor()

    sql = '''INSERT INTO ProductRecords(Name,Amount,Location,Date)
         VALUES(?,?,?,?)
    '''
    cursor.execute(sql, Records)

    con.commit()
