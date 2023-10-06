from django.db import models
from django.core import validators


class Item(models.Model):
    gender_selection = ((1, "男性"), (2, "女性"))  # 男、女を選択できる
    name = models.CharField(
        verbose_name="名前",
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name="年齢",
        validators=[validators.MinLengthValidator(1)],  # リストはバリデーションのルールを定義している　これは最小が１、１未満ならエラー
        blank=True,  # フォームフィールとが空白でもok
        null=True,  # DBのカラムが空白でもいいということ
    )
