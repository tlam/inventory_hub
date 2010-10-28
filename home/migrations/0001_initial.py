# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Home'
        db.create_table('home_home', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tax', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['taxes.Tax'])),
        ))
        db.send_create_signal('home', ['Home'])


    def backwards(self, orm):
        
        # Deleting model 'Home'
        db.delete_table('home_home')


    models = {
        'home.home': {
            'Meta': {'object_name': 'Home'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tax': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['taxes.Tax']"})
        },
        'taxes.tax': {
            'Meta': {'object_name': 'Tax'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'})
        }
    }

    complete_apps = ['home']
