from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship 
from sqlalchemy import String, ForeignKey

class Base(DeclarativeBase):
    pass

class Teacherbase(Base):
    __tablename__ = "teacher"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str| None] = mapped_column(String(100))


class Subjectbase(Base):
    __tablename__ = "subject"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

class Schedulebase(Base):
    __tablename__ = "schedule"
    id: Mapped[int] = mapped_column(primary_key=True)
    lesson_number: Mapped[int] = mapped_column()
    lesson_type: Mapped[str] = mapped_column(String(50))
    day_of_week: Mapped[str] = mapped_column(String(20))
    room: Mapped[str] = mapped_column(String(50))
    week_type: Mapped[str] = mapped_column(String(20))
    lesson_time: Mapped[str] = mapped_column(String(20))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subject.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"))
    subject: Mapped[Subjectbase] = relationship()
    teacher: Mapped[Teacherbase] = relationship()

