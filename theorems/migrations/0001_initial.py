# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-06-10 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Definition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition_name', models.CharField(max_length=255)),
                ('definition', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proof_Definition_Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theorems.Definition')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('answer_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Theorem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theorem_name', models.CharField(max_length=255)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theorems.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Theorem_Proof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theorem_proof', models.TextField()),
                ('theorem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theorems.Theorem')),
            ],
        ),
        migrations.CreateModel(
            name='Theorem_Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theorem_statement', models.TextField()),
                ('theorem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='theorems.Theorem')),
            ],
        ),
        migrations.AddField(
            model_name='theorem_proof',
            name='theorem_statement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theorems.Theorem_Statement'),
        ),
        migrations.AddField(
            model_name='proof_definition_link',
            name='proof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theorems.Theorem_Proof'),
        ),
        migrations.AddField(
            model_name='definition',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theorems.Subject'),
        ),
        migrations.AlterUniqueTogether(
            name='theorem',
            unique_together=set([('theorem_name', 'subject')]),
        ),
        migrations.AlterUniqueTogether(
            name='proof_definition_link',
            unique_together=set([('definition', 'proof')]),
        ),
        migrations.AlterUniqueTogether(
            name='definition',
            unique_together=set([('subject', 'definition_name')]),
        ),
    ]
