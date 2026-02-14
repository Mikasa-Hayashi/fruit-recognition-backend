import json
from pathlib import Path
from sqlalchemy import select
from models.units import Unit
from models.unit_translations import UnitTranslation
from models.nutrients import Nutrient
from models.nutrient_translations import NutrientTranslation
from models.fruits import Fruit
from models.fruit_translations import FruitTranslation

from core.config import settings


async def seed_database(session):

    if not settings.SEED_PATH:
        return {'status': 'file_not_found'}

    with open(settings.SEED_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # =========================
    # UNITS
    # =========================
    for unit_data in data.get('units', []):
        slug = unit_data['slug']

        result = await session.execute(
            select(Unit).where(Unit.slug == slug)
        )
        unit = result.scalar_one_or_none()

        if not unit:
            unit = Unit(slug=slug)
            session.add(unit)
            await session.flush()  # получаем unit.id

        # --- translations ---
        for tr in unit_data.get('unit_translations', []):
            result = await session.execute(
                select(UnitTranslation).where(
                    UnitTranslation.unit_id == unit.id,
                    UnitTranslation.language == tr['language']
                )
            )
            translation = result.scalar_one_or_none()

            if not translation:
                translation = UnitTranslation(
                    unit_id=unit.id,
                    language=tr['language'],
                    short_form=tr['short_form'],
                    full_form=tr['full_form'],
                )
                session.add(translation)
            else:
                translation.short_form = tr['short_form']
                translation.full_form = tr['full_form']

    # =========================
    # NUTRIENTS
    # =========================
    for nutrient_data in data.get('nutrients', []):

        # найти unit по slug
        result = await session.execute(
            select(Unit).where(Unit.slug == nutrient_data['unit_slug'])
        )
        unit = result.scalar_one_or_none()

        if not unit:
            raise Exception(f'Unit {nutrient_data['unit_slug']} not found')

        # найти nutrient
        result = await session.execute(
            select(Nutrient).where(Nutrient.slug == nutrient_data['slug'])
        )
        nutrient = result.scalar_one_or_none()

        if not nutrient:
            nutrient = Nutrient(
                slug=nutrient_data['slug'],
                category=nutrient_data['category'],
                unit_id=unit.id,
                rda=nutrient_data['rda']
            )
            session.add(nutrient)
            await session.flush()
        else:
            nutrient.category = nutrient_data['category']
            nutrient.rda = nutrient_data['rda']
            nutrient.unit_id = unit.id

        # --- translations ---
        for tr in nutrient_data.get('nutrient_translations', []):
            result = await session.execute(
                select(NutrientTranslation).where(
                    NutrientTranslation.nutrient_id == nutrient.id,
                    NutrientTranslation.language == tr['language']
                )
            )
            translation = result.scalar_one_or_none()

            if not translation:
                translation = NutrientTranslation(
                    nutrient_id=nutrient.id,
                    language=tr['language'],
                    name=tr['name'],
                    description=tr['description'],
                )
                session.add(translation)
            else:
                translation.name = tr['name']
                translation.description = tr['description']

    await session.commit()

    return {'status': 'seed_completed'}