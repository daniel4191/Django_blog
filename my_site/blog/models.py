from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # 여기서 사용한 EmailField덕분에, 해당 필드에 이메일을 기입하지 않으면 Enter a valid email address. 라는 에러가 뜸
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    # image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    # 이것으로 인해서 admin에서 관리하는 POST가 어디서 비롯되었는지를 확인 할 수가 있다.
    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    # forms.py 로 overwrite를 하여서 Your name으로 만들거다.
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()  # 마찬가지로 forms.py로 overwrite 예정
    text = models.TextField(max_length=400)  # 마찬가지로 forms.py로 overwrite 예정
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
