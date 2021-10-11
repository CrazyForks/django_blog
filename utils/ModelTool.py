from django.contrib.auth import get_user_model

# https://docs.djangoproject.com/zh-hans/3.2/topics/auth/customizing/#referencing-the-user-model
# get_user_model 容错性更好, 比起直接用 from django.contrib.auth.models import User
User = get_user_model()
