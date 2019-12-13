from django.db import models


class Register(models.Model):
    userID = models.CharField(primary_key=True, max_length=250)
    firstname = models.CharField(max_length=250)
    middlename = models.CharField(max_length=250, blank=True)
    lastname = models.CharField(max_length=250)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, blank=True)
    officephone = models.CharField(max_length=250, blank=True)
    cellphone = models.CharField(max_length=250, blank=True)


class Test_Standard(models.Model):
    standard_ID = models.CharField(max_length=250, primary_key=True)
    standard_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    published_date = models.CharField(max_length=250)


class Service(models.Model):
    service_ID = models.CharField(primary_key=True, max_length=250)
    service_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    is_FI_required = models.CharField(max_length=250)
    FI_frequency = models.CharField(max_length=250)
    standard_ID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)


class Test_Sequence(models.Model):
    sequence_ID = models.CharField(primary_key=True, max_length=250)
    sequence_name = models.CharField(max_length=250)


class Client(models.Model):
    client_ID = models.CharField(primary_key=True, max_length=250)
    client_name = models.CharField(max_length=250)
    client_type = models.CharField(max_length=250)


class Location(models.Model):
    location_ID = models.CharField(primary_key=True, max_length=250)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    fax_number = models.CharField(max_length=250)
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)


class User(models.Model):
    userID = models.CharField(primary_key=True, max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    job_title = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    office_phone = models.CharField(max_length=250)
    cell_phone = models.CharField(max_length=250)
    prefix = models.CharField(max_length=250)
    client_ID = models.ForeignKey(Client, on_delete=models.CASCADE)


class Product(models.Model):
    model_number = models.CharField(primary_key=True, max_length=250)
    product_name = models.CharField(max_length=250)
    cell_technology = models.CharField(max_length=250)
    cell_manufacturer = models.CharField(max_length=250)
    number_of_cells = models.CharField(max_length=250)
    number_of_cells_in_series = models.CharField(max_length=250)
    number_of_series_strings = models.CharField(max_length=250)
    number_of_diodes = models.CharField(max_length=250)
    product_length = models.CharField(max_length=250)
    product_width = models.CharField(max_length=250)
    product_weight = models.CharField(max_length=250)
    superstate_type = models.CharField(max_length=250)
    superstate_manufacturer = models.CharField(max_length=250)
    substrate_type = models.CharField(max_length=250)
    substrate_manufacturer = models.CharField(max_length=250)
    frame_type = models.CharField(max_length=250)
    frame_adhesive = models.CharField(max_length=250)
    encapsulate_type = models.CharField(max_length=250)
    encapsulate_manufacturer = models.CharField(max_length=250)
    junction_box_type = models.CharField(max_length=250)
    junction_box_manufacturer = models.CharField(max_length=250)


class Performance_Data(models.Model):
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence_ID = models.ForeignKey(Test_Sequence, on_delete=models.CASCADE)
    max_system_voltage = models.CharField(max_length=250)
    voc = models.CharField(max_length=250)
    isc = models.CharField(max_length=250)
    vmp = models.CharField(max_length=250)
    imp = models.CharField(max_length=250)
    pmp = models.CharField(max_length=250)
    ff = models.CharField(max_length=250)

    class Meta:
        unique_together = (("model_number", "sequence_ID"),)


class Certificate(models.Model):
    certificate_number = models.CharField(primary_key=True, max_length=250)
    ID = models.CharField(max_length=250)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    report_number = models.CharField(max_length=250)
    issue_date = models.CharField(max_length=250)
    standard_ID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)
    location_ID = models.ForeignKey(Location, on_delete=models.CASCADE)
    model_number = models.ForeignKey(Product, on_delete=models.CASCADE)
