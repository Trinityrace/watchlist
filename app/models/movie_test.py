import unittest
from models import movie
Movie = movie.Movie

class MovieTest (unittest.TestCase):
  '''
  Test case to test behaviuor of the Movie class 
  '''

  def setUp (self):
    '''
    set up method that will run before every test 
    '''
    self.new_movie = Movie (1234, 'Python Must Be Crazy','A Thrilling new Python series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance (self):
      self.assertTrue(isinstance(self.new_movie,Movie))

if __name__ == '__main__':
  unittest.main()