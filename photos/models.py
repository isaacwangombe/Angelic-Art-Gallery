from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()    

    @classmethod
    def update_category(cls, search_term , new_cat):
        try:
            to_update = Categories.objects.get(name = search_term)
            to_update.name = new_cat
            to_update.save()
            return to_update
        except Categories.DoesNotExist:
            print('Category you specified does not exist')

    

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ManyToManyField(Categories)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, new_url):
        try:
            self.image_link = new_url
            self.save()
            return self
        except self.DoesNotExist:
            print('Image you specified does not exist')

    

    @classmethod
    def get_all(cls):
        pics = Images.objects.all()
        return pics

    @classmethod
    def get_image_by_id(cls, id):
        retrieved = Images.objects.get(id = id)
        return retrieved

    @classmethod
    def search_by_category(cls, cat):
        retrieved = cls.objects.filter(category__name__contains=cat) 
        return retrieved 

    @classmethod
    def search_by_location(cls, search_term):
        retrieved = cls.objects.filter(location__city__contains=search_term) 
        return retrieved 



class Locations(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


    @classmethod
    def update_location(cls, search_term , new_loc):
        try:
            to_update = Locations.objects.get(city = search_term)
            to_update.city = new_loc
            to_update.save()
            return to_update
        except Locations.DoesNotExist:
            print('Location you specified does not exist')

    @classmethod
    def get_all(cls):
        cities = Locations.objects.all()
        return cities