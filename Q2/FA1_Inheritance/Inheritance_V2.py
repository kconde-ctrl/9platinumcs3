class Publication: 
  def __init__(self, title: str, author: str):
    self.__title = title
    self.__author = author
  
  def get_title(self):
    return self.__title
    
  def get_author(self):
    return self.__author
    
  def set_title(self, title):
    self.__title = title
    
  def set_author(self, author):
    self.__author = author
    
  def display_info(self):
    print(f"Title: {self._title}")
    print(f"Author: {self._authpr}")

class Book(Publication):
  def __init__(self, title: str, author: str, number_of_pages: int):
    super().__init__(title, author)
    self.set_number_of_pages(number_of_pages)
    
  def get_number_of_pages(self):
    return self.number_of_pages
    
  def set_number_of_pages(self, number_of_pages):
    if number_of_pages <= 0:
      print("The number of pages must be positive")
    else:
      self.number_of_pages = number_of_pages
      
  def display_info(self):
    super().display_info()
    print(f"Number_of_pages: {self._number_of_pages}")

class Magazine(Publication):
  def __init__(self, title, author, issue_number):
    super().__init__(title, author)
    self.set_issue_number(issue_number)
    
  def get_issue_numer(self):
    return self.issue_number
    
  def set_issue_number(self, issue_number):
    if issue_number <= 0:
      print("The issue number must be positive")
    else:
      self._issue_number = issue_number
      
  def display_info(self):
    super().display_info()
    print(f"issue_number: {self._issue_number}")
    
