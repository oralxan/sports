from django.db.models import *
class ContactMessage(Model):
    name = CharField(max_length=100)
    email = EmailField()
    message = TextField()
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

