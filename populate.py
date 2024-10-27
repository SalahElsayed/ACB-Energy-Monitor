# populate.py
import os
import random
from datetime import datetime, timedelta

import django
from django.conf import settings

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acb_demo.settings')
django.setup()

from units.models import ACBUnit, UnitConsumption

def populate():
    # إنشاء وحدات ACB
    units = [
        ACBUnit.objects.create(name='ACB Unit 1', status='active'),
        ACBUnit.objects.create(name='ACB Unit 2', status='active'),
        ACBUnit.objects.create(name='ACB Unit 3', status='inactive'),
        ACBUnit.objects.create(name='ACB Unit 4', status='active'),
        ACBUnit.objects.create(name='ACB Unit 5', status='inactive'),
    ]

    # إنشاء بيانات استهلاك عشوائية
    for unit in units:
        for _ in range(10):  # عدد السجلات لكل وحدة
            energy_consumption = random.uniform(100.0, 500.0)  # استهلاك عشوائي
            temperature = random.uniform(18.0, 30.0)  # درجة حرارة عشوائية
            created_at = datetime.now() - timedelta(days=random.randint(0, 30))  # تاريخ عشوائي في الشهر الماضي

            UnitConsumption.objects.create(
                unit=unit,
                energy_consumption=energy_consumption,
                temperature=temperature,
                created_at=created_at
            )

    print("Sample data created successfully!")

if __name__ == '__main__':
    populate()
