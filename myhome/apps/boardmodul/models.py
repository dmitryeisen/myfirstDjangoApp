from django.db import models

class boardmodul(models.Model):
    boardmodul_title = models.CharField("modulname", max_length = 200)
    boardmodul_text = models.TextField("modulinfo")
    pub_date = models.DateTimeField("publicdate")

    def __str__(self):
        return self.boardmodul_title
class comment(models.Model):
    boardmodul = models.ForeignKey(boardmodul, on_delete = models.CASCADE)
    author_name = models.CharField("authorname", max_length = 50)
    comment_text = models.CharField("commenttext", max_length = 200)
