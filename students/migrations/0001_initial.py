# Generated by Django 2.2.20 on 2021-04-27 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Предмет')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('notes', models.TextField(blank=True, verbose_name='Дополнительные заметки')),
            ],
            options={
                'verbose_name': 'Экзамен',
                'verbose_name_plural': 'Экзамены',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('notes', models.TextField(blank=True, verbose_name='Дополнительные заметки')),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=256, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Отчество')),
                ('birthday', models.DateField(null=True, verbose_name='Дата рождения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('notes', models.TextField(blank=True, verbose_name='Дополнительные заметки')),
            ],
            options={
                'verbose_name': 'Пеподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Name')),
                ('first_name_en', models.CharField(max_length=256, null=True, verbose_name='Name')),
                ('first_name_uk', models.CharField(max_length=256, null=True, verbose_name='Name')),
                ('first_name_ru', models.CharField(max_length=256, null=True, verbose_name='Name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Last Name')),
                ('last_name_en', models.CharField(max_length=256, null=True, verbose_name='Last Name')),
                ('last_name_uk', models.CharField(max_length=256, null=True, verbose_name='Last Name')),
                ('last_name_ru', models.CharField(max_length=256, null=True, verbose_name='Last Name')),
                ('middle_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Father name')),
                ('middle_name_en', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Father name')),
                ('middle_name_uk', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Father name')),
                ('middle_name_ru', models.CharField(blank=True, default='', max_length=256, null=True, verbose_name='Father name')),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Photo')),
                ('ticket', models.CharField(max_length=256, verbose_name='Ticket')),
                ('notes', models.TextField(blank=True, verbose_name='Additional Notes')),
                ('notes_en', models.TextField(blank=True, null=True, verbose_name='Additional Notes')),
                ('notes_uk', models.TextField(blank=True, null=True, verbose_name='Additional Notes')),
                ('notes_ru', models.TextField(blank=True, null=True, verbose_name='Additional Notes')),
                ('student_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Resoult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.IntegerField(null=True, verbose_name='Оценка')),
                ('notes', models.TextField(blank=True, verbose_name='Дополнительные заметки')),
                ('exam', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Exam', verbose_name='Предмет')),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student', verbose_name='Студент')),
                ('teacher', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Результ экзамена',
                'verbose_name_plural': 'Результаты экзаменов',
            },
        ),
        migrations.CreateModel(
            name='MonthJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present_day1', models.BooleanField(default=False)),
                ('present_day2', models.BooleanField(default=False)),
                ('present_day3', models.BooleanField(default=False)),
                ('present_day4', models.BooleanField(default=False)),
                ('present_day5', models.BooleanField(default=False)),
                ('present_day6', models.BooleanField(default=False)),
                ('present_day7', models.BooleanField(default=False)),
                ('present_day8', models.BooleanField(default=False)),
                ('present_day9', models.BooleanField(default=False)),
                ('present_day10', models.BooleanField(default=False)),
                ('present_day11', models.BooleanField(default=False)),
                ('present_day12', models.BooleanField(default=False)),
                ('present_day13', models.BooleanField(default=False)),
                ('present_day14', models.BooleanField(default=False)),
                ('present_day15', models.BooleanField(default=False)),
                ('present_day16', models.BooleanField(default=False)),
                ('present_day17', models.BooleanField(default=False)),
                ('present_day18', models.BooleanField(default=False)),
                ('present_day19', models.BooleanField(default=False)),
                ('present_day20', models.BooleanField(default=False)),
                ('present_day21', models.BooleanField(default=False)),
                ('present_day22', models.BooleanField(default=False)),
                ('present_day23', models.BooleanField(default=False)),
                ('present_day24', models.BooleanField(default=False)),
                ('present_day25', models.BooleanField(default=False)),
                ('present_day26', models.BooleanField(default=False)),
                ('present_day27', models.BooleanField(default=False)),
                ('present_day28', models.BooleanField(default=False)),
                ('present_day29', models.BooleanField(default=False)),
                ('present_day30', models.BooleanField(default=False)),
                ('present_day31', models.BooleanField(default=False)),
                ('date', models.DateField(verbose_name='Дата')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', unique_for_month='date', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Месячный Журнал',
                'verbose_name_plural': 'Месячные журналы',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student', verbose_name='Староста'),
        ),
        migrations.AddField(
            model_name='exam',
            name='exams_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Group', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='exam',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Teacher', verbose_name='Преподаватель'),
        ),
    ]
