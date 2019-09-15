from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader # modifies the load_userfunction by passing in a user_id to the function that queries the database and gets a User with that ID.
def load_user(user_id):
    return User.query.get(int(user_id))



class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count



class Review(db.Model):
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.Time, default = datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    
    def save_review(self):
        db.session.add(self)
        db.session.commit()
        
        
    @classmethod
    def get_reviews(cls, id):
        reviews = Review.query.filter_by(movie_id = id).all()
        return reviews
    
# class Review:

#     all_reviews = []

#     def __init__(self,movie_id,title,imageurl,review):
#         self.movie_id = movie_id
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review


#     def save_review(self):
#         Review.all_reviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()

#     @classmethod
#     def get_reviews(cls,id):

#         response = []

#         for review in cls.all_reviews:
#             if review.movie_id == id:
#                 response.append(review)

#         return response
 
 
 
 
class User(UserMixin,db.Model): # create User class and pass in db.Model as an argument to connect our class to our database and allow communication
    
    __tablename__ = 'users' # allows us to give the tables in our database proper names. if it's not used, SQLAlchemy will assume the tablename is the lowercase of the class name i.e user in this case
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255),unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    reviews = db.relationship('Review', backref = 'user', lazy = "dynamic")
    
    
    @property # decorator to create a write only class property, password.
    
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self): # this method makes it easier to debug the application
        
        return f'User {self.username}'
    
    
    
class Role(db.Model): # class to define all the different roles
    __tablename__ = 'roles'
    
    # create two columns for the id and the name
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy="dynamic") # virtual column to connect with foreign key
    
    def __repr__(self):
        return f'User {self.name}'
    
