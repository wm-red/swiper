from django.db import models

# Create your models here.
GENDERS=(
    ('male', '男性'),
    ('female', '女')
)
LOCATIONS=(
        ('北京', '北京'),
        ('上海', '上海'),
        ('深圳', '深圳'),
        ('成都', '成都'),
        ('西安', '西安'),
        ("武汉", "武汉"),
        ("沈阳", "沈阳")
)

class User(models.Model):
    phonenum = models.CharField(max_length=16, unique=True, verbose_name='手机号')
    nickname = models.CharField(max_length=20, db_index=True, verbose_name='用户名')
    gender= models.CharField(max_length=10, choices=GENDERS, verbose_name='性别')
    birthday = models.DateField(default='2001-01-01', verbose_name='出生日期')
    avatar = models.CharField(max_length=256, verbose_name='个人头像')
    location = models.CharField(max_length=10, choices=LOCATIONS, verbose_name='居住地')
    def to_dict(self):
        return {
            'id':self.id,
            'phonenum':self.phonenum,
            'gender':self.gender,
            'birthday':self.birthday,
            'avatar':self.avatar,
            'location':self.location
        }