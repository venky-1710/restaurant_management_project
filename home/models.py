from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # ✅

    def __str__(self):
        return self.name

from django.db import models

class Feedback(models.Model):
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} - {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name



class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class RestaurantLocation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state} {self.zip_code}"




class RestaurantDetails(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)  # New field

    def __str__(self):
        return self.name



class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    opening_hours = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  # ✅ New field

    def __str__(self):
        return self.name




class Feedback(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.submitted_at.strftime('%Y-%m-%d')}"



class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.title
        

class Customer(models.Model):
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional: Name of the customer"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Optional: Phone number for contact or SMS updates"
    )
    email = models.EmailField(
        blank=True,
        null=True,
        help_text="Optional: Email for receipts or marketing"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the customer record was created"
    )

    def __str__(self):
        # Show something meaningful even if fields are empty
        if self.name:
            return self.name
        elif self.phone:
            return self.phone
        elif self.email:
            return self.email
        return f"Customer #{self.id}"


from django.db import models

class Special(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)  # defaults to today's date

    def __str__(self):
        return self.name

























