from flask import Flask, jsonify, request,render_template
import dask.dataframe as dd
from dask_sql import Context
from datetime import datetime
from sqlalchemy import sql
import pytz


app = Flask(__name__)



@app.route('/',methods=["GET", "POST"])
def index():
    return render_template('date_page.html')

@app.route('/get_results', methods=['POST']) 
def get_results(): 
    pass
    # if request.method == "POST":
    #     formatt = "%Y-%m-%dT%H:%M"
    #     start_date = datetime.strptime(request.form.get("start"),formatt).astimezone(pytz.utc)

    #     end_date = datetime.strptime(request.form.get("end"),formatt).astimezone(pytz.utc)

    #     if start_date <= end_date:
    #         # st = pd.to_datetime(str(start_date).split('+')[0])
    #         # en = pd.to_datetime(str(end_date).split('+')[0] )
    #         ddf = dd.read_sql('test_table1', r"mysql://root:root@localhost:3001/test_db","Lon")
    #         c = Context()
    #         c.create_table('tablee',ddf)
    #         result = c.sql('''
    #             SELECT * FROM tablee WHERE `Date/Time` BETWEEN "2014-04-01 04:11:00" AND "2014-04-01 06:11:00"
    #         ''')
    #         print(result.compute())
    #         return result.head().to_json()

    #         # return result.head()
    # return {"Error": "Query not executed."}
  
@app.route('/execute_query', methods=['GET','POST']) 
def execute_query(): 
    if request.method == "POST":
        formatt = "%Y-%m-%dT%H:%M"
        start_date = datetime.strptime(request.form.get("start"),formatt).astimezone(pytz.utc)

        end_date = datetime.strptime(request.form.get("end"),formatt).astimezone(pytz.utc)

        if start_date <= end_date:
            # query_text = f'''Lat, Lon FROM test_table1 WHERE Date/Time BETWEEN {str(str(start_date).split('+')[0])} AND {str(str(end_date).split('+')[0])} GROUP BY Base;'''
            st = str(start_date).split('+')[0]
            en = str(end_date).split('+')[0]   

            # return jsonify({'st':str(type(st)),"en":en})
            # query_text =f'''* FROM test_table1 WHERE `Date/Time` BETWEEN "{st}" AND "{en}"'''

            ddf = dd.read_sql('test_table1', r"mysql://root:root@localhost:3001/test_db","Lat")
            filtered_data = ddf[(ddf['Date/Time'] >= st) & (ddf['Date/Time'] <= en)].set_index("Date/Time")

            # sql_query = sql.select(sql.text(query_text))

            # result = dd.read_sql(sql=sql_query,con=r"mysql://root:root@localhost:3001/test_db",index_col="Lon")
            return jsonify(filtered_data.to_dict())
        else:
            return jsonify({"Error":"Select Proper Interval"})
  
  

@app.route('/pa', methods=['GET','POST']) 
def pa(): 
    ddf = dd.read_sql('test_table2_lookup', r"mysql://root:root@localhost:3001/test_db","LocationID")
    return ddf.head().to_json()


if __name__ == "__main__":
    app.run(debug=True)