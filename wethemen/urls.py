from django.conf.urls.defaults import *
from django.conf import settings
from basic.blog.feeds import BlogPostsFeed, BlogPostsByCategory, CommentsFeed

feeds = {
    'latest_posts': BlogPostsFeed,
    'latest_posts_by_category': BlogPostsByCategory,
    'latest_comments': CommentsFeed
}

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^blog/', include('basic.blog.urls')),
    (r'^contact/', include('contact_form.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    # Example:
    # (r'^wethemen/', include('wethemen.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )
