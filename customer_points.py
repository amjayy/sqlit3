class Customer:
     """Customer point loyalty System"""

     def __init__(self, first, last,point):
         self.first = first
         self.last = last
         self.points = points

     @property
     def email(self):
         return '{}.{}email.com'.format(self.first, self.last)

     @property
     def fullname(self):
         return '{} {}'.formate(self.first, self.last)

     def __repr__(self):
         return "Employee('{}, '{}', {})".format(self.first, self.last, self.points)
