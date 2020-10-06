# Generated by Django 3.1.1 on 2020-09-12 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golden', '0010_auto_20200912_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('design_produto', models.TextField()),
                ('data_produto', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('imagem', models.ImageField(upload_to='images/produtos')),
                ('nome_categoria', models.CharField(choices=[('Blusa de Moletom', 'Blusa de Moletom'), ('Calça de Sarja', 'Calça de Sarja'), ('Camisetas', 'Camisetas'), ('Bonés', 'Bonés'), ('Blusa corta-vento', 'Blusa corta-vento'), ('Calça de Moletom', 'Calça de Moletom'), ('Acessórios', 'Acessórios'), ('Jaquetas', 'Jaquetas'), ('Calçados', 'Calçados')], max_length=50, verbose_name='Categoria')),
                ('tamanho_um', models.CharField(choices=[('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=5, verbose_name='Tamanhos')),
                ('tamanho_dois', models.CharField(choices=[('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=5, verbose_name='Tamanhos')),
                ('tamanho_tres', models.CharField(choices=[('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=5, verbose_name='Tamanhos')),
                ('tamanho_quatro', models.CharField(choices=[('P', 'P'), ('M', 'M'), ('G', 'G'), ('GG', 'GG')], max_length=5, verbose_name='Tamanhos')),
            ],
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
