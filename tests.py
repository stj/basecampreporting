import unittest
from project import Project

class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.username = "apitest"
        self.password = "apitest"
        self.url = "http://apitesting.basecamphq.com/"
        self.project_id = 2849305

        self.project = Project(self.url, self.project_id, self.username, self.password)

    def test_latest_message(self):
        self.assertEqual("This is the newest message",
                         self.project.messages[0].title)

    def test_latest_comment(self):
        self.assertEqual("This is the latest comment",
                         self.project.comments[0].body)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
