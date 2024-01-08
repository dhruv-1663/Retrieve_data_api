# from flask import Flask, jsonify, request,render_template
# from flask_sqlalchemy import SQLAlchemy 

# app = Flask(__name__)

# # db  = SQLAlchemy() 
# # db_cred = { 
# #     'user': 'root',         
# #     'pass': 'root',      
# #     'host': 'localhost:3001',     
# #     'name': 'test_db'   
# # } 
# # app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_cred['user']}:{db_cred['pass']}@{db_cred['host']}//{db_cred['name']}" 
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db.init_app(app)

# @app.route('/',methods=["GET", "POST"])
# def index():
#     return render_template('date_page.html')

# @app.route('/get_results', methods=['POST']) 
# def get_results(): 
      
#     result = db.engine.execute(request.get_json()['query']) 
#     response = {} 
#     i = 1
   
#     for each in result: 
#         response.update({f'Record {i}': list(each)}) 
#         i+= 1
  
#     return response 
  
# @app.route('/execute_query', methods=['POST']) 
# def execute_query(): 
  
#     try: 
#         db.engine.execute(request.get_json()['query']) 
#     except: 
#         return {"message": "Request could not be completed."} 
  
#     return {"message": "Query executed successfully."}

# @app.route('/pa', methods=['GET']) 
# def pa(): 
#     conn = db.engine.connect()
#     result = conn.execute(text(sql)).fetchall()
#         # for rows in result:
#         #     print(rows)
#     return result


# if __name__ == "__main__":
#     app.run(debug=True)