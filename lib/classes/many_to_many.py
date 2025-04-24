from collections import Counter

class Article:
    all = []  

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        author.articles().append(self)
        magazine.articles().append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            raise AttributeError("Title can't be changed after instantiation")
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value


class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed after instantiation")
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        """Creates and returns a new Article associated with this author and magazine"""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns unique magazine categories or None if no articles"""
        if not self._articles:
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        """Returns unique list of authors who have written for this magazine"""
        return list({article.author for article in self._articles})

    def article_titles(self):
        """Returns list of article titles or None if no articles"""
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        """Returns authors with >2 articles or None if none exist"""
        if not self._articles:
            return None
        author_counts = Counter(article.author for article in self._articles)
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None