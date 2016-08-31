from django.conf.urls import url
from . import views


# url 的第一個參數接受規則表示式（Regular expression），用來定義 URL Pattern，
# 第二個參數表示該對應至哪個函式，
# 第三個參數用來定義這個 URL Pattern 的名稱，
# 某些地方若要參考這個定義，可以透過名稱來指定參考。
# 可以看到，有地方改用了(?P<name>pattern)的樣式撰寫，
# 此語法是Python語言的Regular expression operations，
# 其中的name是指群組名稱，而pattern是正規表示式

# ex: /polls/
# url(r'^$', views.index, name='index'),
# ex: /polls/5/
# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
# ex: /polls/5/results/
# url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
# ex: /polls/5/vote/
# url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^abc/$', views.post_list2, name='post_list2'),
]