from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# bagian upload file
UPLOAD_FOLDER = 'app/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#seeder
seeder = FlaskSeeder()
seeder.init_app(app,db)

#model
from app.model import prodi, daftarSidang, berkasSidang

#routes
from app.route import routes, routeProdi



# # Create a working task queue  
# def background_task(n):
#     try:
#         """ Function that 
#         returns len(n) and 
#         simulates a delay """

#         delay = 2

#         print("Task running")
#         print(f"Simulating a {delay} second delay")

#         time.sleep(delay)

#         print(len(n))
#         print("Task complete")

#         return len(n)
#     except Exception as e:
#         print(e)
#     print(f"tes {n}")
#     return "tes"



# @app.route("/task")
# def jj():
#     # try:

#         banyak = 0
#         if request.args.get("n"):

#             job = q.enqueue(background_task, request.args.get("n"))
#             # banyak = len(q)
#             return f"Task ({job.id}) added to queue at {job.enqueued_at}"
#         banyak = len(q)
#         return f"No value for count provided {banyak}"
#     # except HorseMonitorTimeoutException as e:
#         print(e)
