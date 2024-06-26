from django.db import models

# Create your models here.
class Person(models.Model):
    person_text = models.CharField(max_length=200)

    def __str__(self):
        return self.person_text


class PersonDetail(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    person_subtext = models.TextField()

    def __str__(self):
        return f"{self.person_subtext[:50]}..."
    

class PersonsImage(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='persons/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Event(models.Model):
    event_text = models.CharField(max_length=200)

    def __str__(self):
        return self.event_text


class EventDetail(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_subtext = models.TextField()

    def __str__(self):
        return f"{self.event_subtext[:50]}..."
    

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Food(models.Model):
    food_text = models.CharField(max_length=200)

    def __str__(self):
        return self.food_text


class FoodDetail(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_subtext = models.TextField()

    def __str__(self):
        return f"{self.food_subtext[:50]}..."
    

class FoodImage(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='foods/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Clothe(models.Model):
    clothe_text = models.CharField(max_length=200)

    def __str__(self):
        return self.clothe_text


class ClotheDetail(models.Model):
    clothe = models.ForeignKey(Clothe, on_delete=models.CASCADE)
    clothe_subtext = models.TextField()

    def __str__(self):
        return f"{self.clothe_subtext[:50]}..."
    

class ClotheImage(models.Model):
    clothe = models.ForeignKey(Clothe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='clothes/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Livelihood(models.Model):
    livelihood_text = models.CharField(max_length=200)

    def __str__(self):
        return self.livelihood_text


class LivelihoodDetail(models.Model):
    livelihood = models.ForeignKey(Livelihood, on_delete=models.CASCADE)
    livelihood_subtext = models.TextField()

    def __str__(self):
        return f"{self.livelihood_subtext[:50]}..."
    

class LivelihoodImage(models.Model):
    livelihood = models.ForeignKey(Livelihood, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='livelihoods/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Culture(models.Model):
    culture_text = models.CharField(max_length=200)

    def __str__(self):
        return self.culture_text


class CultureDetail(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    culture_subtext = models.TextField()

    def __str__(self):
        return f"{self.culture_subtext[:50]}..."
    

class CultureImage(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cultures/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Medicine(models.Model):
    medicine_text = models.CharField(max_length=200)

    def __str__(self):
        return self.medicine_text


class MedicineDetail(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    medicine_subtext = models.TextField()

    def __str__(self):
        return f"{self.medicine_subtext[:50]}..."
    

class MedicineImage(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='medicines/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Invention(models.Model):
    invention_text = models.CharField(max_length=200)

    def __str__(self):
        return self.invention_text


class InventionDetail(models.Model):
    invention = models.ForeignKey(Invention, on_delete=models.CASCADE)
    invention_subtext = models.TextField()

    def __str__(self):
        return f"{self.invention_subtext[:50]}..."
    

class InventionImage(models.Model):
    invention = models.ForeignKey(Invention, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='inventions/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title