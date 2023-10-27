from django.db import models
from django.core import validators


class User(models.Model):
    gender_selection = ((1, "男性"), (2, "女性"), (3, "その他"))  # 男、女を選択できる
    name = models.CharField(
        verbose_name="名前",
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name="年齢",
        validators=[validators.MinLengthValidator(1)],  # バリデーションのルールを定義している　これは最小が１、１未満ならエラー
        blank=True,  # フォームフィールとが空白でもok
        null=True,  # DBのカラムが空白でもいいということ
    )
    gender = models.IntegerField(verbose_name="性別", choices=gender_selection, default=1)  # choicesは選択できる

    email = models.EmailField(
        verbose_name="メールアドレス入力",
        max_length=254,
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name="電話番号",
        max_length=12,
    )


def __str__(self):
    return self.name


class Meta:
    verbose_name = "ユーザー"
