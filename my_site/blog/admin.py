from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

# post admin창에 각각의 필터 모습을 보여주기


class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'date')
    # 관리자 페이지에서 등록 목록을 볼때 조회되는 항목 카테고리
    list_display = ('title', 'date', 'author')
    # 이것은 post에서 title을 작성하면 slug에 자동으로 변환되어 생성되게끔하는 기능
    # 주의 점은 slug로 전환해줄 대상이 되는 title의 뒤에 컴마를 안붙여주면
    # ERRORS: <class 'blog.admin.PostAdmin'>: (admin.E029) The value of 'prepopulated_fields["slug"]' must be a list or tuple.
    # 이런 에러가 뜬다.
    # 재밌는 점은, title에서 slug로 자동 전환될때 영어만 인식하고 변환해주는 것 같다.
    prepopulated_fields = {'slug': ('title',)}


# 이 클래스로 인해서 admin 창에서 user_name과 어디서 post를 확인 할 수가 있게 되었다.
# 물론 admin.site.register에 등록을 했기 때문에.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
