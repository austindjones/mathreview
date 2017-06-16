from django.contrib import admin

# Register your models here.
from .models import Subject
from .models import Theorem
from .models import Theorem_Statement
from .models import Theorem_Proof
from .models import Definition
from .models import Proof_Definition_Link
from .models import Question
from .models import Keyword
from .models import Theorem_Keyword_Link

admin.site.register(Subject)
admin.site.register(Theorem)
admin.site.register(Theorem_Statement)
admin.site.register(Theorem_Proof)
admin.site.register(Definition)
admin.site.register(Proof_Definition_Link)
admin.site.register(Question)
admin.site.register(Keyword)
admin.site.register(Theorem_Keyword_Link)
