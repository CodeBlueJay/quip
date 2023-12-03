from django.db import models

# Challenges should only be allowed to be submitted from trusted sources
# they can be used for XSS attacks w/ current setup

class Challenge(models.Model):
    fields = [
        "description",
        "function_name",
        "function_args",
        "cases",
    ]
    
    description = models.CharField(max_length=1000)
    function_name = models.CharField(max_length=40)
    function_args = models.JSONField()
    cases = models.JSONField()
    
    def __str__(self):
        return f"challenge #{self.id:0>4} | {self.function_name}"
    
    def json(self):
        return str({name:getattr(self, name) for name in self.fields})