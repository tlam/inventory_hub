# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Town'
        db.create_table('geography_town', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('geography', ['Town'])

        # Adding unique constraint on 'Country', fields ['name']
        db.create_unique('geography_country', ['name'])

        # Adding unique constraint on 'City', fields ['name']
        db.create_unique('geography_city', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'City', fields ['name']
        db.delete_unique('geography_city', ['name'])

        # Removing unique constraint on 'Country', fields ['name']
        db.delete_unique('geography_country', ['name'])

        # Deleting model 'Town'
        db.delete_table('geography_town')


    models = {
        'geography.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'geography.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'geography.town': {
            'Meta': {'ordering': "['name']", 'object_name': 'Town'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['geography']
