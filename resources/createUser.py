from flask_restful import Resource
class createUser(Resource):
    def get(self):
        return {"message":"User created successfully !"}
