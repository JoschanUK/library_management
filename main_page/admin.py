from django.contrib import admin
from .models import booklist
from .models import member_records
from .models import comment
from .models import book_borrowed
# Register your models here.
admin.site.register(booklist)
admin.site.register(member_records)
admin.site.register(comment)
admin.site.register(book_borrowed)
