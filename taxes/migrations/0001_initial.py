# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tax'
        db.create_table('taxes_tax', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('percent', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal('taxes', ['Tax'])


    def backwards(self, orm):
        
        # Deleting model 'Tax'
        db.delete_table('taxes_tax')


    models = {
        'taxes.tax': {
            'Meta': {'object_name': 'Tax'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'percent': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'})
        }
    }

    complete_apps = ['taxes']
