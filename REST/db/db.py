from models import Room, Staff, Tenant


DB = {}


def fillup_db():
    DB['rooms'].append(Room(12, 1, 'cleaning', 1200))
    DB['rooms'].append(Room(8, 2, 'rented', 8000))
    DB['rooms'].append(Room(33, 2, 'rented', 3300))
    DB['rooms'].append(Room(666, 6, 'rented', 666))
    DB['rooms'].append(Room(721, 6, 'available', 3300))

    DB['staff'].append(Staff('Jerry', '123123123XR', 'bellboy', 100))
    DB['staff'].append(Staff('Adam', '234234234XC', 'driver', 6000))
    DB['staff'].append(Staff('Gabriel', '345345345XU', 'doorman', 3000))

    DB['tenants'].append(Tenant('Brown', '123456789XU', 29, 'w',
                                {
                                    "city": "Portland",
                                    "street": "SE 26th Ave"
                                }, 8))
    DB['tenants'].append(Tenant('Johnson', '234567890XU', 35, 'm',
                                {
                                    "city": "Dayton",
                                    "street": "Banker St, 250"
                                }, 33))
    DB['tenants'].append(Tenant('Gray', '345678901XU', 48, '-',
                                {
                                    "city": "Portsmouth",
                                    "street": "Sunrise Ave, 22"
                                }, 666))
