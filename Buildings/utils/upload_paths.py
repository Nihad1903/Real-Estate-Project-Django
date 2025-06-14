def office_image_upload_to(instance, filename):
    print("office_id:", instance.office.id)
    print("owner_id:", instance.office.owner.id)
    owner_id = instance.office.owner.id if instance.office and instance.office.owner else 'unknown'
    office_id = instance.office.id
    return f'office/{owner_id}/{office_id}/{filename}'


def flat_image_upload_to(instance, filename):
    owner_id = instance.flat.owner.id
    flat_id = instance.flat.id
    return f'flat/{owner_id}/{flat_id}/{filename}'


def garden_house_image_upload_to(instance, filename):
    owner_id = instance.garden_house.owner.id
    garden_house_id = instance.garden_house.id
    return f'garden_house/{owner_id}/{garden_house_id}/{filename}'


def garage_image_upload_to(instance, filename):
    owner_id = instance.garage.owner.id
    garage_id = instance.garage.id
    return f'garage/{owner_id}/{garage_id}/{filename}'


def land_image_upload_to(instance, filename):
    owner_id = instance.land.owner.id
    land_id = instance.land.id
    return f'land/{owner_id}/{land_id}/{filename}'