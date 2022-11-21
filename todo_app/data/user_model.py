#Not sure if this is needed? Different method then the suggested one? 

class User(db.Document):
    name = db.StringField()
    password = db.StringField()
    email = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "email": self.email}

    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)



