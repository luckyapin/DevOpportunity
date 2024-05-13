from sqlalchemy import MetaData, Integer, String, ForeignKey, Column, Table, Boolean, Numeric

metadata = MetaData()

# -----------------------------filters-----------------------------

city = Table(
    'city',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('city', String)
)

work_location = Table(
    'work_location',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('work_location', String)
)

employment_type = Table(
    'employment_type',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('employment_type', String)
)

specialization = Table(
    'specialization',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('specialization', String)
)

education = Table(
    'education',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('education', String)
)

work_experience = Table(
    'work_experience',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('work_experience', String)
)

work_schedule = Table(
    'work_schedule',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('work_schedule', String)
)

programming_language = Table(
    'programming_language',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('programming_language', String)
)

# -----------------------------user-----------------------------

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('is_active', Boolean, nullable=False),
    Column('is_verified', Boolean, nullable=False),
    Column('is_superuser', Boolean, nullable=False),
    Column('hashed_password', String, nullable=False),
)

favorite_filters = Table(
    'favorite_filters',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user', Integer, ForeignKey('user.id')),
    Column('salary_range_min', Numeric),
    Column('salary_range_max', Numeric),
    Column('city', Integer, ForeignKey('city.id')),
    Column('work_location', Integer, ForeignKey('work_location.id')),
    Column('employment_type', Integer, ForeignKey('employment_type.id')),
    Column('specialization', Integer, ForeignKey('specialization.id')),
    Column('education', Integer, ForeignKey('education.id')),
    Column('work_experience', Integer, ForeignKey('work_experience.id')),
    Column('work_schedule', Integer, ForeignKey('work_schedule.id')),
    Column('programming_language', Integer, ForeignKey('programming_language.id')),

)
# -----------------------------vacancy-----------------------------

vacancy = Table(
    'vacancy',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('description', String),
    Column('salary_range_min', Numeric),
    Column('salary_range_max', Numeric),
    Column('city', Integer, ForeignKey('city.id')),
    Column('work_location', Integer, ForeignKey('work_location.id')),
    Column('employment_type', Integer, ForeignKey('employment_type.id')),
    Column('specialization', Integer, ForeignKey('specialization.id')),
    Column('education', Integer, ForeignKey('education.id')),
    Column('work_experience', Integer, ForeignKey('work_experience.id')),
    Column('work_schedule', Integer, ForeignKey('work_schedule.id')),
    Column('programming_language', Integer, ForeignKey('programming_language.id')),
)

favorite_vacancy = Table(
    'favorite_vacancy',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user', Integer, ForeignKey('user.id')),
    Column('vacancy', Integer, ForeignKey('vacancy.id')),
)



