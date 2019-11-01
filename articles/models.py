from django.db import models

# Reporter(1) - Article(N)
# reporter - name


class Reporter(models.Model):
    name = models.CharField(max_length=10)


class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.title}'


# Article(1) - Comment(N)
# comment - content


class Comment(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


    # on_delete
    # 1. CASCADE: 글이 삭제되었을 때 모든 댓글을 삭제
    # 2. PROTECT: 댓글이 존재하면 글 삭제 안됨.
    # 3. SET_NULL : 글이 삭제되면 NULL로 치환(NOT NULL일 경우 사용 불가)
    # 4. SET_DEFAULT : 디폴트 값으로 치환.