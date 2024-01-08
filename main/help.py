from sqlalchemy import sql
# from dask_sql import Context
import dask.dataframe as dd

# dbEngine = sqlalchemy.create_engine("mysql://root:root@localhost:3001/test_db")
# conn = dbEngine.connect()

# metadata = sqlalchemy.MetaData()
# metadata.reflect(bind=dbEngine)

# t = sqlalchemy.Table('test_table1',metadata,autoload_with=dbEngine)

# print(conn.execute(t.select()).fetchall())

# sql_query = sql.select(sql.text('* FROM test_table1 WHERE `Date/Time` BETWEEN "2014-04-01 04:11:00" AND "2014-04-01 06:11:00"'))
ddf = dd.read_sql('test_table1', r"mysql://root:root@localhost:3001/test_db","index")

start_date = '2014-04-01 04:11:00'
end_date = '2014-04-01 06:11:0'

# start_date = pd.to_datetime(start_date)
# end_date = pd.to_datetime(end_date)

# ddf['Date/Time'] = pd.to_datetime(ddf['Date/Time'])
filtered_data = ddf[(ddf['Date/Time'] >= start_date) & (ddf['Date/Time'] <= end_date)]
print(filtered_data.head().to_dict(orient='records'))

# ddf["DT"] = dd.to_datetime(ddf["Date/Time"].dt.time.astype(str))
# ddf.columns = ddf.columns.astype(str)
# ddf.loc[(ddf['Date/Time'] > start_date)&(ddf['Date/Time']< end_date)].compute()

# # Display the result
# print(ddf.head())
