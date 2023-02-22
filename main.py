from flask import Flask,app
from flask_restful import Resource,Api,abort,reqparse
from flask_mysqldb import MySQL
from flask_cors import CORS,cross_origin
import MySQLdb.cursors

app = Flask(__name__)

api = Api(app)
cors = CORS(app)


app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="todo_db"


mysql = MySQL(app)

todo_put_args = reqparse.RequestParser()
todo_put_args.add_argument("username",type=str,help="name of the todo user",required=True)
todo_put_args.add_argument("todoname",type=str,help="name of the todo",required=True)
todo_put_args.add_argument("is_deleted",type=str,help="todo is deleted or not",required=True)


######################################## abort actions ##################################################





###################################### end of abort actions ###############################################



class Todo(Resource):
 
    @cross_origin()
    def get(self,action):
        if action == "all":
            cursor= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(""" select * from new_table""")
            data = cursor.fetchall()
            mysql.connection.commit()
            cursor.close()

        else:
            data = self.get_one(action)


        


        return {"data":data}

    def get_one(self,action):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(""" select * from new_table where id=%s""",(action))
        data = cursor.fetchone()
        mysql.connection.commit()
        cursor.close()

        return data




            

    


    @cross_origin()
    def post(self,action):
        if action=="fetch":
            args=todo_put_args.parse_args()
            username = args['username']
            todoname = args['todoname']
            is_deleted = args['is_deleted']

            cursor= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("""insert into new_table (username,todoname,is_deleted) values(%s,%s,%s)""",(username,todoname,is_deleted))
            mysql.connection.commit()
            cursor.close()


            return {"status":"todo added succesfully"},200


    @cross_origin()
    def delete(self,action):
        
        

        cursor= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("""delete from new_table where id=%s""",(action))
        mysql.connection.commit()
        cursor.close()


        return {"status":"deleted succesfully"}
        






api.add_resource(Todo,"/api/todo/<string:action>")


if __name__ == "__main__":
    app.run(debug=True)






