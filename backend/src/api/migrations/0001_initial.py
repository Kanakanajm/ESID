# Generated by Django 3.2.3 on 2021-07-12 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Gaussian', 'Gaussian')], max_length=10)),
                ('min', models.FloatField()),
                ('max', models.FloatField()),
                ('mean', models.FloatField()),
                ('deviation', models.FloatField()),
                ('value', models.FloatField()),
            ],
            options={
                'verbose_name': 'Distribution',
                'verbose_name_plural': 'Distributions',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('contact_rate', models.DecimalField(decimal_places=3, max_digits=3)),
            ],
            options={
                'verbose_name': 'Measure',
                'verbose_name_plural': 'Measures',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('metadata', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_rate', models.FloatField()),
            ],
            options={
                'verbose_name': 'Restriction',
                'verbose_name_plural': 'Restrictions',
            },
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('number_of_groups', models.IntegerField()),
                ('number_of_nodes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.group')),
                ('interventions', models.ManyToManyField(to='api.Intervention')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.node')),
            ],
        ),
        migrations.CreateModel(
            name='SimulationCompartment',
            fields=[
                ('distribution_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.distribution')),
                ('compartment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.compartment')),
            ],
            bases=('api.distribution',),
        ),
        migrations.CreateModel(
            name='SimulationNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenario_node', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.scenarionode')),
                ('comparments', models.ManyToManyField(to='api.SimulationCompartment')),
            ],
        ),
        migrations.CreateModel(
            name='SimulationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('compartments', models.ManyToManyField(to='api.Compartment')),
                ('parameters', models.ManyToManyField(to='api.Parameter')),
            ],
        ),
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('start_day', models.DateField()),
                ('number_of_days', models.IntegerField()),
                ('nodes', models.ManyToManyField(to='api.SimulationNode')),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.scenario')),
            ],
        ),
        migrations.AddField(
            model_name='scenario',
            name='nodes',
            field=models.ManyToManyField(to='api.ScenarioNode'),
        ),
        migrations.AddField(
            model_name='scenario',
            name='simulation_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='simulation_model', to='api.simulationmodel'),
        ),
        migrations.AddField(
            model_name='intervention',
            name='restriction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.restriction'),
        ),
        migrations.CreateModel(
            name='ScenarioParameter',
            fields=[
                ('distribution_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.distribution')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='parameter', to='api.parameter')),
            ],
            bases=('api.distribution',),
        ),
        migrations.AddField(
            model_name='scenarionode',
            name='parameters',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.scenarioparameter'),
        ),
    ]
