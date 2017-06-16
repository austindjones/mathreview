from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    def __str__(self):
        return self.subject_name

class Theorem(models.Model):
    theorem_name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.theorem_name
    @property
    def sorted_proof_set(self):
        return list(self.theorem_proof_set.order_by('id'))
    class Meta:
        unique_together = ('theorem_name', 'subject')
   
 
class Theorem_Statement(models.Model):
    theorem = models.OneToOneField(Theorem, on_delete=models.CASCADE)
    theorem_statement = models.TextField()
    def __str__(self):
        return self.theorem_statement

class Theorem_Proof(models.Model):
    theorem = models.ForeignKey(Theorem, on_delete=models.CASCADE)
    theorem_statement = models.ForeignKey(Theorem_Statement, on_delete=models.CASCADE)
    theorem_proof = models.TextField()
    def __str__(self):
        return self.theorem_proof[:255]

class Definition(models.Model):
    definition_name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    definition = models.TextField()
    def __str__(self):
        return str( (self.definition_name, self.subject) )
    class Meta:
        unique_together = ('subject','definition_name')

class Proof_Definition_Link(models.Model):
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)
    proof = models.ForeignKey(Theorem_Proof, on_delete=models.CASCADE)
    def __str__(self):
        return str( (self.definition,self.proof) )
    class Meta:
        unique_together = ('definition','proof')

class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    def __str__(self):
        return self.question_text

class Keyword(models.Model):
    keyword_text = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.keyword_text


class Theorem_Keyword_Link(models.Model):
    theorem = models.ForeignKey(Theorem, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    def __str__(self):
        return str( (self.theorem, self.keyword) )
    class Meta:
        unique_together = ('theorem', 'keyword')
