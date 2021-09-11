from django.db import models


class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(null=True,default='no_image.png',upload_to='images')
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def price_in_tooman(self):
        k = 1000
        m = k * k
        if self.price / m > 1:
            if self.price % m == 0:
                return str(int(self.price / m)) + ' میلیون تومان'
            else:
                return str(int(self.price / m)) + ' میلیون و ' + str(
                    int((self.price % m) / k)) + ' هزار تومان'
        else:
            return str(int(self.price / k)) + ' هزار تومان'