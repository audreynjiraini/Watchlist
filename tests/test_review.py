import unittest
from app.models import Review,User
from app import db

class ReviewTest(unittest.TestCase):
    '''
   Test Class to test the behaviour of the Review class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.user_Audrey = User(username = 'Audrey', password = 'potato', email = 'audrey@ms.com')
        self.new_review = Review(movie_id = 12345,movie_title = 'Review for movies',image_path = "https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review = 'This movie is the best thing since sliced bread', user = self.user_Audrey)
        
        
    def tearDown(self):
        Review.query.delete()
        User.query.delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))
        
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.movie_title,'Review for movies')
        self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_Audrey)


    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)


    def test_get_review_by_id(self):

        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)