from django import forms
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=10,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'row': 5,
                'cols': 50,
            }
        )
    )
    class Meta: # meta 는 정보에 의한 정보이다, 카메라의 명도, 조리개, 습도 등등, MODEL 이 없음!!!!
        model = Article
        fields = ('title', 'content',)
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'class': 'my-title',
        #             'placeholder': 'Enter the title!',
        #         }
        #     )
        # }
# class ArticleForm(forms.Form):  <- 위에 있는 부분과 다른 것은 수정 에서 드러난다
    # title = forms.CharField(max_length=20)
    # content = forms.CharField(widget=forms.Textarea)
    # title = forms.CharField(
    #     max_length=20,
    #     label='제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'my-title',
    #             'placeholder': 'Enter the title!',
    #         }
    #     )
    # )
    # content = forms.CharField(
    #     label='내용',
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'my-content',
    #             'placeholder': 'Enter the content!',
    #             'rows': 5,
    #             'column': 50,
    #         }
    #     )
    # )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)